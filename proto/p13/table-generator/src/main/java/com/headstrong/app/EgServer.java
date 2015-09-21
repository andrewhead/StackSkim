package com.headstrong.app;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.io.OutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.InetSocketAddress;
import java.net.URLDecoder;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import net.sf.jsqlparser.JSQLParserException;
import net.sf.jsqlparser.parser.CCJSqlParserUtil;
import net.sf.jsqlparser.statement.Statement;
import net.sf.jsqlparser.expression.Expression;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;


public class EgServer {

    public static void main(String[] args) throws Exception {
        int portNumber = 8000;
        if (args.length >= 1) {
            portNumber = Integer.parseInt(args[0]);
        }
        HttpServer server = HttpServer.create(new InetSocketAddress(portNumber), 0);
        server.createContext("/", new QueryHandler());
        server.setExecutor(null);
        server.start();
    }

    public static String getTable(String sql) {

        // Parse the SQL statement
        Statement stmt = null;
        try {
            stmt = CCJSqlParserUtil.parse(sql);
        } catch (JSQLParserException e) {
            System.out.println("Invalid SQL. Exiting");
            return null;
        }

        // Generate data from the SQL statement
        if (stmt == null) {
            return null;
        }

        // Extract all column names and expressions from the SQL
        SelectColumnExtractor colExtractor = new SelectColumnExtractor();
        ArrayList<String> columnNames = colExtractor.getColumnNames(stmt);
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        EgExpression rootExpression = expExtractor.visit(stmt);
        ArrayList<EgExpression> leafExpressions = expExtractor.getLeafExpressions();

        // Generate a truth table of the combinations of expression values
        TruthTable truthTable = new TruthTable(rootExpression, leafExpressions);
        truthTable.evaluate();

        // Get expression conditions for selected and 'almost selected' rows
        ArrayList<Evaluation> relevantEvaluations = new ArrayList<Evaluation>();
        ArrayList<Evaluation> selectedEvaluations = truthTable.getTrueEvaluations();
        relevantEvaluations.addAll(selectedEvaluations);
        relevantEvaluations.addAll(truthTable.getOneOffEvaluations());

        // Serialize table into Json
        Gson gson = new GsonBuilder()
            .registerTypeAdapter(EgTable.class, new EgTableSerializer())
            .registerTypeAdapter(EgRow.class, new EgRowSerializer())
            .create();

        EgTable startTable = buildTableForEvaluations(leafExpressions, relevantEvaluations);
        EgTable selectedTable = buildTableForEvaluations(leafExpressions, selectedEvaluations);

        Object tables = new Tables(startTable, selectedTable);
        return gson.toJson(tables);
    }

    static EgTable buildTableForEvaluations(ArrayList<EgExpression> expressions, 
            ArrayList<Evaluation> evaluations) {

        // Get ordered list of names of columns used in expressions
        ArrayList<String> expressionColumnNames = new ArrayList<String>();
        ColumnNameFinder colNameFinder = new ColumnNameFinder();
        if (evaluations.size() > 0) {
            for (EgExpression expr:expressions) {
                String name = colNameFinder.getName(expr.getJsqlParserExpression());
                expressionColumnNames.add(name);
            }
        }

        // Detect the types for columns found
        ArrayList<ColumnType> expressionColumnTypes = new ArrayList<ColumnType>();
        ColumnTypeFinder colTypeFinder = new ColumnTypeFinder();
        for (String colName:expressionColumnNames) {
            ColumnType colType = colTypeFinder.getType(colName, expressions);
            expressionColumnTypes.add(colType);
        }

        // Generate row of fake data for each of the evaluations of the WHERE clause
        ArrayList<EgRow> rows = new ArrayList<EgRow>();
        DataGenerator dataGenerator = new DataGenerator();
        for (Evaluation eval:evaluations) {
            ArrayList<Object> cells = new ArrayList<Object>();
            ArrayList<Boolean> inputValues = eval.getValues();
            for (int i = 0; i < expressions.size(); i++) {
                EgExpression expr = expressions.get(i);
                Expression jsqlExpression = expr.getJsqlParserExpression();
                boolean input = inputValues.get(i).booleanValue();
                Object data = dataGenerator.generateData(jsqlExpression, input);
                cells.add(data);
            }
            rows.add(new EgRow(expressionColumnNames, cells.toArray()));
        }
        EgTable table = new EgTable(expressionColumnNames, expressionColumnTypes);
        for (EgRow row:rows) {
            table.addRow(row);
        }

        return table;
    }

    /**
     * Container of the two types of tables we want to return
     */
    static class Tables {
        private EgTable original;
        private EgTable selected;
        public Tables(EgTable originalTable, EgTable selectedTable) {
            this.original = originalTable;
            this.selected = selectedTable;
        }
    }

    static class QueryHandler implements HttpHandler {

        public void handle(HttpExchange t) throws IOException {
            String queryString = t.getRequestURI().getQuery();
            Map<String, String> params = queryToMap(queryString);
            String sql = params.get("sql");
            System.out.println("Received SQL: " + sql);
            String response = "callback(" + getTable(sql) + ");";
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }

        /* 
         * REUSE: this method comes from
         * http://stackoverflow.com/questions/11640025/java-httpserver-httpexchange-get 
         * */
        private Map<String, String> queryToMap(String query){
            Map<String, String> result = new HashMap<String, String>();
            for (String param : query.split("&")) {
                String pair[] = param.split("=", 2);
                String decodedPair[] = new String[pair.length];
                for (int i = 0; i < pair.length; i++) {
                    try {
                        decodedPair[i] = URLDecoder.decode(pair[i], "UTF-8");
                    } catch (UnsupportedEncodingException e) {
                        decodedPair[i] = pair[i];
                    }
                }
                if (pair.length > 1) {
                    result.put(decodedPair[0], decodedPair[1]);
                } else{
                    result.put(decodedPair[0], "");
                }
            }
            return result;
        }

    }

}

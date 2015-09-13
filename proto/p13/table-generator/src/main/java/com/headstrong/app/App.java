package com.headstrong.app;

import java.util.ArrayList;

import net.sf.jsqlparser.JSQLParserException;
import net.sf.jsqlparser.parser.CCJSqlParserUtil;
import net.sf.jsqlparser.statement.Statement;


public class App {

    public static void main(String[] args) {
        try {
            Statement stmt = CCJSqlParserUtil.parse("SELECT id, email FROM tab1 WHERE email = 'hello' AND id > 1");
            SelectColumnExtractor colExtractor = new SelectColumnExtractor();
            SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
            System.out.println(colExtractor.getColumnNames(stmt));
            // System.out.println(stmt.toString());
        } catch (JSQLParserException e) {

        }
    }

}

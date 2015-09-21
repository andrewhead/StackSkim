package com.headstrong.app;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;

import net.sf.jsqlparser.JSQLParserException;
import net.sf.jsqlparser.parser.CCJSqlParserUtil;
import net.sf.jsqlparser.statement.select.Select;
import net.sf.jsqlparser.statement.select.SelectVisitor;
import net.sf.jsqlparser.statement.select.PlainSelect;
import net.sf.jsqlparser.statement.select.WithItem;
import net.sf.jsqlparser.statement.select.SetOperationList;
import net.sf.jsqlparser.statement.select.SelectItem;
import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.ExpressionVisitor;
import net.sf.jsqlparser.statement.Statement;
import net.sf.jsqlparser.statement.StatementVisitorAdapter;

import net.sf.jsqlparser.expression.NullValue;
import net.sf.jsqlparser.expression.Function;
import net.sf.jsqlparser.expression.BinaryExpression;
import net.sf.jsqlparser.expression.SignedExpression;
import net.sf.jsqlparser.expression.JdbcParameter;
import net.sf.jsqlparser.expression.JdbcNamedParameter;
import net.sf.jsqlparser.expression.DoubleValue;
import net.sf.jsqlparser.expression.LongValue;
import net.sf.jsqlparser.expression.DateValue;
import net.sf.jsqlparser.expression.TimeValue;
import net.sf.jsqlparser.expression.TimestampValue;
import net.sf.jsqlparser.expression.Parenthesis;
import net.sf.jsqlparser.expression.StringValue;
import net.sf.jsqlparser.expression.CaseExpression;
import net.sf.jsqlparser.expression.WhenClause;
import net.sf.jsqlparser.expression.AllComparisonExpression;
import net.sf.jsqlparser.expression.AnyComparisonExpression;
import net.sf.jsqlparser.expression.CastExpression;
import net.sf.jsqlparser.expression.AnalyticExpression;
import net.sf.jsqlparser.expression.WithinGroupExpression;
import net.sf.jsqlparser.expression.ExtractExpression;
import net.sf.jsqlparser.expression.IntervalExpression;
import net.sf.jsqlparser.expression.OracleHierarchicalExpression;
import net.sf.jsqlparser.expression.JsonExpression;
import net.sf.jsqlparser.expression.UserVariable;
import net.sf.jsqlparser.expression.NumericBind;
import net.sf.jsqlparser.expression.KeepExpression;
import net.sf.jsqlparser.expression.operators.arithmetic.Addition;
import net.sf.jsqlparser.expression.operators.arithmetic.BitwiseAnd;
import net.sf.jsqlparser.expression.operators.arithmetic.BitwiseOr;
import net.sf.jsqlparser.expression.operators.arithmetic.BitwiseXor;
import net.sf.jsqlparser.expression.operators.arithmetic.Concat;
import net.sf.jsqlparser.expression.operators.arithmetic.Division;
import net.sf.jsqlparser.expression.operators.arithmetic.Modulo;
import net.sf.jsqlparser.expression.operators.arithmetic.Multiplication;
import net.sf.jsqlparser.expression.operators.arithmetic.Subtraction;
import net.sf.jsqlparser.expression.operators.conditional.AndExpression;
import net.sf.jsqlparser.expression.operators.conditional.OrExpression;
import net.sf.jsqlparser.expression.operators.relational.Between;
import net.sf.jsqlparser.expression.operators.relational.EqualsTo;
import net.sf.jsqlparser.expression.operators.relational.ExistsExpression;
import net.sf.jsqlparser.expression.operators.relational.GreaterThan;
import net.sf.jsqlparser.expression.operators.relational.GreaterThanEquals;
import net.sf.jsqlparser.expression.operators.relational.InExpression;
import net.sf.jsqlparser.expression.operators.relational.IsNullExpression;
import net.sf.jsqlparser.expression.operators.relational.LikeExpression;
import net.sf.jsqlparser.expression.operators.relational.Matches;
import net.sf.jsqlparser.expression.operators.relational.MinorThan;
import net.sf.jsqlparser.expression.operators.relational.MinorThanEquals;
import net.sf.jsqlparser.expression.operators.relational.NotEqualsTo;
import net.sf.jsqlparser.expression.operators.relational.RegExpMatchOperator;
import net.sf.jsqlparser.expression.operators.relational.RegExpMySQLOperator;
import net.sf.jsqlparser.schema.Column;
import net.sf.jsqlparser.statement.select.SubSelect;


public class SelectExpressionExtractor extends StatementVisitorAdapter
    implements SelectVisitor, ExpressionVisitor {

    private EgExpression mRoot;
    private ArrayList<EgExpression> mLeafExpressions;
    private HashMap<Expression, EgExpression> mExpressions = new HashMap<Expression, EgExpression>();

    public EgExpression visit(Statement statement) {
        mRoot = null;
        mLeafExpressions = new ArrayList<EgExpression>();
        statement.accept(this);
        return mRoot;
    }

    @Override
    public void visit(AndExpression andExpression) {
        EgAndExpression expr = new EgAndExpression(andExpression, andExpression.toString());
        saveExpression(expr, andExpression);
        expr.getChildren().addAll(visitConditional(andExpression));
    }

    @Override
    public void visit(OrExpression orExpression) {
        EgOrExpression expr = new EgOrExpression(orExpression, orExpression.toString());
        saveExpression(expr, orExpression);
        expr.getChildren().addAll(visitConditional(orExpression));
    }

    @Override
    public void visit(Parenthesis parenthesis) {
        // When we arrive at a parenthesis, visit what's inside, ignoring this as an expression
        // We need to map this parentheses expression to the EgExpression we create for the child
        Expression childExpr = parenthesis.getExpression();
        childExpr.accept(this);
        mExpressions.put(parenthesis, mExpressions.get(childExpr));
    }

    private EgExpression visitLeafExpression(Expression sqlParserExpression) {
        EgExpression expr = new EgExpression(sqlParserExpression, sqlParserExpression.toString());
        mExpressions.put(sqlParserExpression, expr);
        mLeafExpressions.add(expr);
        saveExpression(expr, sqlParserExpression);
        return expr;
    }

    private ArrayList<EgExpression> visitConditional(BinaryExpression condExpr) {
        Expression left = condExpr.getLeftExpression();
        Expression right = condExpr.getRightExpression();
        left.accept(this);
        right.accept(this);
        ArrayList<EgExpression> children = new ArrayList<EgExpression>();
        children.add(mExpressions.get(left));
        children.add(mExpressions.get(right));
        return children;
    }

    private void saveExpression(EgExpression egExpr, Expression expr) {
        mExpressions.put(expr, egExpr);
        // If this is the first time visiting a condition, then save it as the tree root.
        if (mRoot == null) {
            mRoot = egExpr;
        }
    }

    @Override
    public void visit(PlainSelect plainSelect) {
        if (plainSelect.getWhere() != null) {
            plainSelect.getWhere().accept(this);
        }
    }

    public ArrayList<EgExpression> getLeafExpressions() {
        return mLeafExpressions;
    }

    @Override
    public void visit(NullValue nullValue) {
        EgExpression expr = visitLeafExpression(nullValue);
    }

    @Override
    public void visit(Function function) {
        EgExpression expr = visitLeafExpression(function);
    }

    @Override
    public void visit(SignedExpression signedExpression) {
        EgExpression expr = visitLeafExpression(signedExpression);
    }

    @Override
    public void visit(JdbcParameter jdbcParameter) {
        EgExpression expr = visitLeafExpression(jdbcParameter);
    }

    @Override
    public void visit(JdbcNamedParameter jdbcNamedParameter) {
        EgExpression expr = visitLeafExpression(jdbcNamedParameter);
    }

    @Override
    public void visit(DoubleValue doubleValue) {
        EgExpression expr = visitLeafExpression(doubleValue);
    }
    
    @Override
    public void visit(LongValue longValue) {
        EgExpression expr = visitLeafExpression(longValue);
    }
    
    @Override
    public void visit(DateValue dateValue) {
        EgExpression expr = visitLeafExpression(dateValue);
    }

    @Override
    public void visit(TimeValue timeValue) {
        EgExpression expr = visitLeafExpression(timeValue);
    }

    @Override
    public void visit(TimestampValue timestampValue) {
        EgExpression expr = visitLeafExpression(timestampValue);
    }

    @Override
    public void visit(StringValue stringValue) {
        EgExpression expr = visitLeafExpression(stringValue);
    }

    @Override
    public void visit(Addition addition) {
        EgExpression expr = visitLeafExpression(addition);
    }

    @Override
    public void visit(Division division) {
        EgExpression expr = visitLeafExpression(division);
    }

    @Override
    public void visit(Multiplication multiplication) {
        EgExpression expr = visitLeafExpression(multiplication);
    }

    @Override
    public void visit(Subtraction subtraction) {
        EgExpression expr = visitLeafExpression(subtraction);
    }

    @Override
    public void visit(Between between) {
        EgExpression expr = visitLeafExpression(between);
    }

    @Override
    public void visit(EqualsTo equalsTo) {
        EgExpression expr = visitLeafExpression(equalsTo);
    }

    @Override
    public void visit(GreaterThan greaterThan) {
        EgExpression expr = visitLeafExpression(greaterThan);
    }

    @Override
    public void visit(GreaterThanEquals greaterThanEquals) {
        EgExpression expr = visitLeafExpression(greaterThanEquals);
    }

    @Override
    public void visit(InExpression inExpression) {
        EgExpression expr = visitLeafExpression(inExpression);
    }

    @Override
    public void visit(IsNullExpression isNullExpression) {
        EgExpression expr = visitLeafExpression(isNullExpression);
    }

    @Override
    public void visit(LikeExpression likeExpression) {
        EgExpression expr = visitLeafExpression(likeExpression);
    }

    @Override
    public void visit(MinorThan minorThan) {
        EgExpression expr = visitLeafExpression(minorThan);
    }

    @Override
    public void visit(MinorThanEquals minorThanEquals) {
        EgExpression expr = visitLeafExpression(minorThanEquals);
    }

    @Override
    public void visit(NotEqualsTo notEqualsTo) {
        EgExpression expr = visitLeafExpression(notEqualsTo);
    }

    @Override
    public void visit(Column tableColumn) {
        EgExpression expr = visitLeafExpression(tableColumn);
    }

    @Override
    public void visit(SubSelect subSelect) {
        EgExpression expr = visitLeafExpression(subSelect);
    }

    @Override
    public void visit(CaseExpression caseExpression) {
        EgExpression expr = visitLeafExpression(caseExpression);
    }

    @Override
    public void visit(WhenClause whenClause) {
        EgExpression expr = visitLeafExpression(whenClause);
    }

    @Override
    public void visit(ExistsExpression existsExpression) {
        EgExpression expr = visitLeafExpression(existsExpression);
    }

    @Override
    public void visit(AllComparisonExpression allComparisonExpression) {
        EgExpression expr = visitLeafExpression(allComparisonExpression);
    }

    @Override
    public void visit(AnyComparisonExpression anyComparisonExpression) {
        EgExpression expr = visitLeafExpression(anyComparisonExpression);
    }

    @Override
    public void visit(Concat concat) {
        EgExpression expr = visitLeafExpression(concat);
    }

    @Override
    public void visit(Matches matches) {
        EgExpression expr = visitLeafExpression(matches);
    }

    @Override
    public void visit(BitwiseAnd bitwiseAnd) {
        EgExpression expr = visitLeafExpression(bitwiseAnd);
    }

    @Override
    public void visit(BitwiseOr bitwiseOr) {
        EgExpression expr = visitLeafExpression(bitwiseOr);
    }

    @Override
    public void visit(BitwiseXor bitwiseXor) {
        EgExpression expr = visitLeafExpression(bitwiseXor);
    }
    
    @Override
    public void visit(CastExpression cast) {
        EgExpression expr = visitLeafExpression(cast);
    }

    @Override
    public void visit(Modulo modulo) {
        EgExpression expr = visitLeafExpression(modulo);
    }

    @Override
    public void visit(AnalyticExpression aexpr) {
        EgExpression expr = visitLeafExpression(aexpr);
    }
    
    @Override
    public void visit(WithinGroupExpression wgexpr) {
        EgExpression expr = visitLeafExpression(wgexpr);
    }

    @Override
    public void visit(ExtractExpression eexpr) {
        EgExpression expr = visitLeafExpression(eexpr);
    }

    @Override
    public void visit(IntervalExpression iexpr) {
        EgExpression expr = visitLeafExpression(iexpr);
    }

    @Override
    public void visit(OracleHierarchicalExpression oexpr) {
        EgExpression expr = visitLeafExpression(oexpr);
    }

    @Override
    public void visit(RegExpMatchOperator rexpr) {
        EgExpression expr = visitLeafExpression(rexpr);
    }
    
    @Override
    public void visit(JsonExpression jsonExpr) {
        EgExpression expr = visitLeafExpression(jsonExpr);
    }

    @Override
    public void visit(RegExpMySQLOperator regExpMySQLOperator) {
        EgExpression expr = visitLeafExpression(regExpMySQLOperator);
    }
   
    @Override
    public void visit(UserVariable var) {
        EgExpression expr = visitLeafExpression(var);
    }
    
    @Override
    public void visit(NumericBind bind) {
        EgExpression expr = visitLeafExpression(bind);
    }
    
    @Override
    public void visit(KeepExpression aexpr) {
        EgExpression expr = visitLeafExpression(aexpr);
    }
    
    @Override
    public void visit(Select select) {
        select.getSelectBody().accept(this);
    }

    @Override
    public void visit(SetOperationList setOpList) {}

    @Override
    public void visit(WithItem withItem) {}

}

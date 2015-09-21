package com.headstrong.app;

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

    private EgExpression visitLeafExpression(Expression sqlParserExpression) {
        EgExpression exp = new EgExpression(sqlParserExpression, sqlParserExpression.toString());
        mExpressions.put(sqlParserExpression, exp);
        mLeafExpressions.add(exp);
        // If this is the first time visiting a condition, then save it as the tree root.
        if (mRoot == null) {
            mRoot = exp;
        }
        return exp;
    }

    public ArrayList<EgExpression> getLeafExpressions() {
        return mLeafExpressions;
    }

    @Override
    public void visit(AndExpression andExpression) {
        EgAndExpression exp = new EgAndExpression(andExpression, andExpression.toString());
        mExpressions.put(andExpression, exp);
        if (mRoot == null) {
            mRoot = exp;
        }
        Expression left = andExpression.getLeftExpression();
        Expression right = andExpression.getRightExpression();
        left.accept(this);
        right.accept(this);
        ArrayList<EgExpression> andChildren = exp.getChildren();
        andChildren.add(mExpressions.get(left));
        andChildren.add(mExpressions.get(right));
    }

    @Override
    public void visit(NullValue nullValue) {
        EgExpression exp = visitLeafExpression(nullValue);
    }

    @Override
    public void visit(Function function) {
        EgExpression exp = visitLeafExpression(function);
    }

    @Override
    public void visit(SignedExpression signedExpression) {
        EgExpression exp = visitLeafExpression(signedExpression);
    }

    @Override
    public void visit(JdbcParameter jdbcParameter) {
        EgExpression exp = visitLeafExpression(jdbcParameter);
    }

    @Override
    public void visit(JdbcNamedParameter jdbcNamedParameter) {
        EgExpression exp = visitLeafExpression(jdbcNamedParameter);
    }

    @Override
    public void visit(DoubleValue doubleValue) {
        EgExpression exp = visitLeafExpression(doubleValue);
    }
    
    @Override
    public void visit(LongValue longValue) {
        EgExpression exp = visitLeafExpression(longValue);
    }
    
    @Override
    public void visit(DateValue dateValue) {
        EgExpression exp = visitLeafExpression(dateValue);
    }

    @Override
    public void visit(TimeValue timeValue) {
        EgExpression exp = visitLeafExpression(timeValue);
    }

    @Override
    public void visit(TimestampValue timestampValue) {
        EgExpression exp = visitLeafExpression(timestampValue);
    }

    @Override
    public void visit(Parenthesis parenthesis) {
        EgExpression exp = visitLeafExpression(parenthesis);
    }

    @Override
    public void visit(StringValue stringValue) {
        EgExpression exp = visitLeafExpression(stringValue);
    }

    @Override
    public void visit(Addition addition) {
        EgExpression exp = visitLeafExpression(addition);
    }

    @Override
    public void visit(Division division) {
        EgExpression exp = visitLeafExpression(division);
    }

    @Override
    public void visit(Multiplication multiplication) {
        EgExpression exp = visitLeafExpression(multiplication);
    }

    @Override
    public void visit(Subtraction subtraction) {
        EgExpression exp = visitLeafExpression(subtraction);
    }

    @Override
    public void visit(OrExpression orExpression) {
        EgExpression exp = visitLeafExpression(orExpression);
    }

    @Override
    public void visit(Between between) {
        EgExpression exp = visitLeafExpression(between);
    }

    @Override
    public void visit(EqualsTo equalsTo) {
        EgExpression exp = visitLeafExpression(equalsTo);
    }

    @Override
    public void visit(GreaterThan greaterThan) {
        EgExpression exp = visitLeafExpression(greaterThan);
    }

    @Override
    public void visit(GreaterThanEquals greaterThanEquals) {
        EgExpression exp = visitLeafExpression(greaterThanEquals);
    }

    @Override
    public void visit(InExpression inExpression) {
        EgExpression exp = visitLeafExpression(inExpression);
    }

    @Override
    public void visit(IsNullExpression isNullExpression) {
        EgExpression exp = visitLeafExpression(isNullExpression);
    }

    @Override
    public void visit(LikeExpression likeExpression) {
        EgExpression exp = visitLeafExpression(likeExpression);
    }

    @Override
    public void visit(MinorThan minorThan) {
        EgExpression exp = visitLeafExpression(minorThan);
    }

    @Override
    public void visit(MinorThanEquals minorThanEquals) {
        EgExpression exp = visitLeafExpression(minorThanEquals);
    }

    @Override
    public void visit(NotEqualsTo notEqualsTo) {
        EgExpression exp = visitLeafExpression(notEqualsTo);
    }

    @Override
    public void visit(Column tableColumn) {
        EgExpression exp = visitLeafExpression(tableColumn);
    }

    @Override
    public void visit(SubSelect subSelect) {
        EgExpression exp = visitLeafExpression(subSelect);
    }

    @Override
    public void visit(CaseExpression caseExpression) {
        EgExpression exp = visitLeafExpression(caseExpression);
    }

    @Override
    public void visit(WhenClause whenClause) {
        EgExpression exp = visitLeafExpression(whenClause);
    }

    @Override
    public void visit(ExistsExpression existsExpression) {
        EgExpression exp = visitLeafExpression(existsExpression);
    }

    @Override
    public void visit(AllComparisonExpression allComparisonExpression) {
        EgExpression exp = visitLeafExpression(allComparisonExpression);
    }

    @Override
    public void visit(AnyComparisonExpression anyComparisonExpression) {
        EgExpression exp = visitLeafExpression(anyComparisonExpression);
    }

    @Override
    public void visit(Concat concat) {
        EgExpression exp = visitLeafExpression(concat);
    }

    @Override
    public void visit(Matches matches) {
        EgExpression exp = visitLeafExpression(matches);
    }

    @Override
    public void visit(BitwiseAnd bitwiseAnd) {
        EgExpression exp = visitLeafExpression(bitwiseAnd);
    }

    @Override
    public void visit(BitwiseOr bitwiseOr) {
        EgExpression exp = visitLeafExpression(bitwiseOr);
    }

    @Override
    public void visit(BitwiseXor bitwiseXor) {
        EgExpression exp = visitLeafExpression(bitwiseXor);
    }
    
    @Override
    public void visit(CastExpression cast) {
        EgExpression exp = visitLeafExpression(cast);
    }

    @Override
    public void visit(Modulo modulo) {
        EgExpression exp = visitLeafExpression(modulo);
    }

    @Override
    public void visit(AnalyticExpression aexpr) {
        EgExpression exp = visitLeafExpression(aexpr);
    }
    
    @Override
    public void visit(WithinGroupExpression wgexpr) {
        EgExpression exp = visitLeafExpression(wgexpr);
    }

    @Override
    public void visit(ExtractExpression eexpr) {
        EgExpression exp = visitLeafExpression(eexpr);
    }

    @Override
    public void visit(IntervalExpression iexpr) {
        EgExpression exp = visitLeafExpression(iexpr);
    }

    @Override
    public void visit(OracleHierarchicalExpression oexpr) {
        EgExpression exp = visitLeafExpression(oexpr);
    }

    @Override
    public void visit(RegExpMatchOperator rexpr) {
        EgExpression exp = visitLeafExpression(rexpr);
    }
    
    @Override
    public void visit(JsonExpression jsonExpr) {
        EgExpression exp = visitLeafExpression(jsonExpr);
    }

    @Override
    public void visit(RegExpMySQLOperator regExpMySQLOperator) {
        EgExpression exp = visitLeafExpression(regExpMySQLOperator);
    }
   
    @Override
    public void visit(UserVariable var) {
        EgExpression exp = visitLeafExpression(var);
    }
    
    @Override
    public void visit(NumericBind bind) {
        EgExpression exp = visitLeafExpression(bind);
    }
    
    @Override
    public void visit(KeepExpression aexpr) {
        EgExpression exp = visitLeafExpression(aexpr);
    }
    
    @Override
    public void visit(PlainSelect plainSelect) {
        if (plainSelect.getWhere() != null) {
            plainSelect.getWhere().accept(this);
        }
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

package com.headstrong.app;

import net.sf.jsqlparser.parser.CCJSqlParserUtil;
import net.sf.jsqlparser.JSQLParserException;
import net.sf.jsqlparser.statement.Statement;


/**
 * Convenience class for faster parsing of SQL
 */
public class TestJsqlParser {

    public static Statement parse(String sql) {
        try {
            return CCJSqlParserUtil.parse(sql);
        } catch (JSQLParserException e) {
            return null;
        }
    }

}


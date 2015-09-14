package com.headstrong.app;


import net.sf.jsqlparser.expression.Expression;


public class EgAndExpression extends EgExpression {

    public EgAndExpression(Expression jsqlParserExpression, String text) {
        super(jsqlParserExpression, text);
    }

    @Override
    public boolean evaluate() {
        for (EgExpression child: this.getChildren()) {
            if (child.evaluate() == false) {
                return false;
            }
        }
        return true;
    }

}

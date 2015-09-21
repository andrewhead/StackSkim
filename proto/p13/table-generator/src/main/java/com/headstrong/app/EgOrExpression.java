package com.headstrong.app;


import net.sf.jsqlparser.expression.Expression;


public class EgOrExpression extends EgExpression {

    public EgOrExpression(Expression jsqlParserExpression, String text) {
        super(jsqlParserExpression, text);
    }

    @Override
    public boolean evaluate() {
        for (EgExpression child: this.getChildren()) {
            if (child.evaluate() == true) {
                return true;
            }
        }
        return false;
    }

}

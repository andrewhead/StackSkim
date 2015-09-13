package com.headstrong.app;


public class AndExpression extends Expression {

    public AndExpression(String text) {
        super(text);
    }

    @Override
    public boolean evaluate() {
        for (Expression child: this.getChildren()) {
            if (child.evaluate() == false) {
                return false;
            }
        }
        return true;
    }

}

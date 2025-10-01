class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression: str):
        if not expression:
            return None

        tokens = expression.strip().split()
        result = self._evaluate_infix(tokens)
        return result

    def _evaluate_infix(self, tokens: list):
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(values, operators)

                operators.append(token)

            else:
                try:
                    values.append(float(token))

                except ValueError:
                    raise ValueError(f"Invalid token: {token}")

        while operators:
            self._apply_operator(values, operators)

        if len(values) != 1:
            raise ValueError("Invalid expression!")

        return values[0]

    def _apply_operator(self, values, operators):
        if not operators:
            return None

        operator = operators.pop()

        if len(values) < 2:
            raise ValueError(f"Not enough operands for operator: {operator}")

        b = values.pop()
        a = values.pop()

        values.append(self.operators[operator](a, b))

class Solve:
    @staticmethod
    def solve(input_v):
        if not type(input_v) is dict:
            return input_v
        if len(input_v)<1:
            return input_v
        key = next(iter(input_v))
        output_v = key
        input_v = input_v[key]
        while type(input_v) is dict:
            if len(input_v)<1:
                break
            key = next(iter(input_v))
            output_v = {key: output_v}
            input_v = input_v[key]
        if type(input_v) is str:
            output_v = {input_v: output_v}
        return output_v
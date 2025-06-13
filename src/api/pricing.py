model_pricing_per_1m = {
    "eu.anthropic.claude-3-7-sonnet-20250219-v1:0": dict(input=6.0, output=30.0)
}


def get_cost(model_id: str, input_tokens: int, output_tokens: int) -> float:
    if model_id in model_pricing_per_1m:
        return (
            model_pricing_per_1m[model_id]["input"] * input_tokens / 1e6
            + model_pricing_per_1m[model_id]["output"] * output_tokens / 1e6
        )
    else:
        raise ValueError(f"Model {model_id} not found in model_pricing_per_1m")

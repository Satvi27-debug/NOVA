"""
ai_concepts.py
==============
Module containing educational demonstrations of foundational AI, ML,
and Deep Learning concepts using rule-based logic and standard arithmetic.

PRD Compliance:
- FR-13: Rule-based activity recommendation based on hour/time of day.
- FR-14: Simplified, non-trained perceptron calculation (inputs, weights, bias, step activation).
- Educational distinction between rule-based logic, untrainded arithmetic, and real ML training.
"""

from datetime import datetime
from typing import List, Tuple, Optional, Dict, Any


# =====================================================================
# FR-13: Rule-Based Decision System & Decision Tree Analogy
# =====================================================================

def recommend_activity(hour: Optional[int] = None, user_name: str = "Friend") -> str:
    """
    Recommends an activity based on the hour of the day using explicit
    if-elif-else rules, demonstrating a rule-based expert system / decision tree.

    Args:
        hour (Optional[int]): Hour in 24-hour format (0-23). If None, current hour is used.
        user_name (str): The active session user's name.

    Returns:
        str: Formatted recommendation and educational explanation.
    """
    if hour is None:
        hour = datetime.now().hour

    # Rule-based decision logic
    if 5 <= hour < 12:
        period = "Morning"
        activity = "Have a healthy breakfast, plan top priorities, and tackle challenging creative work."
    elif 12 <= hour < 17:
        period = "Afternoon"
        activity = "Enjoy a nutritious lunch, stay hydrated, and focus on steady development tasks."
    elif 17 <= hour < 22:
        period = "Evening"
        activity = "Take a brisk walk, unwind with family or friends, and step away from screens."
    else:
        period = "Night"
        activity = "Prepare for restful sleep, reflect on today's progress, and recharge."

    response = (
        f"Assistant: [{period} Recommendation for {user_name}]\n"
        f"  Current Hour: {hour:02d}:00\n"
        f"  Suggested Activity: {activity}\n\n"
        f"  [AI Concept Note]\n"
        f"  This recommendation uses a Rule-Based Expert System (decision tree logic).\n"
        f"  The hour feature is evaluated against predefined threshold rules to classify\n"
        f"  the appropriate response, illustrating explicit condition-based AI."
    )
    return response


# =====================================================================
# FR-14: Perceptron (Artificial Neuron) & Deep Learning Concept Demo
# =====================================================================

# Fixed weights and bias for educational perceptron demonstration
DEFAULT_WEIGHTS: List[float] = [0.6, 0.4, -0.5]
DEFAULT_BIAS: float = -0.2


def step_activation(weighted_sum: float) -> int:
    """
    Heaviside step activation function:
        f(x) = 1 if x > 0 else 0

    Args:
        weighted_sum (float): Total input signal including bias.

    Returns:
        int: Binary output (1 or 0).
    """
    return 1 if weighted_sum > 0 else 0


def calculate_neuron(
    inputs: List[float],
    weights: List[float],
    bias: float
) -> Dict[str, Any]:
    """
    Performs forward propagation through a single artificial neuron.

    Args:
        inputs (List[float]): Numeric input features (x1, x2, ...).
        weights (List[float]): Synaptic weights (w1, w2, ...).
        bias (float): Threshold bias term (b).

    Returns:
        Dict[str, Any]: Detailed breakdown of the forward pass.
    """
    products = [round(x * w, 4) for x, w in zip(inputs, weights)]
    dot_product = sum(products)
    weighted_sum = round(dot_product + bias, 4)
    output = step_activation(weighted_sum)

    return {
        "inputs": inputs,
        "weights": weights,
        "bias": bias,
        "products": products,
        "dot_product": round(dot_product, 4),
        "weighted_sum": weighted_sum,
        "output": output,
    }


def multi_layer_analogy(inputs: List[float]) -> str:
    """
    Demonstrates a conceptual 2-layer network (Hidden Layer + Output Neuron)
    using plain arithmetic to illustrate deep learning forward propagation.
    """
    # Hidden Layer Neuron 1 & Neuron 2 weights and biases
    h1_weights = [0.5, -0.3, 0.8][:len(inputs)]
    h1_bias = -0.1
    h2_weights = [-0.4, 0.7, 0.2][:len(inputs)]
    h2_bias = 0.0

    h1_res = calculate_neuron(inputs, h1_weights, h1_bias)
    h2_res = calculate_neuron(inputs, h2_weights, h2_bias)

    # Output Layer Neuron receives activations from hidden layer: [h1_res["output"], h2_res["output"]]
    hidden_outputs = [float(h1_res["output"]), float(h2_res["output"])]
    out_weights = [0.9, 0.6]
    out_bias = -0.5
    final_res = calculate_neuron(hidden_outputs, out_weights, out_bias)

    explanation = (
        f"\n  [Optional Hidden Layer Analogy (2-Layer Network)]\n"
        f"  Layer 1 (Hidden Neurons):\n"
        f"    - Neuron H1 Output: {h1_res['output']} (Sum: {h1_res['weighted_sum']})\n"
        f"    - Neuron H2 Output: {h2_res['output']} (Sum: {h2_res['weighted_sum']})\n"
        f"  Layer 2 (Output Neuron):\n"
        f"    - Inputs from Hidden Layer: {hidden_outputs}\n"
        f"    - Final Network Output: {final_res['output']} (Sum: {final_res['weighted_sum']})"
    )
    return explanation


def perceptron_demo(
    custom_inputs: Optional[List[float]] = None,
    interactive: bool = True
) -> str:
    """
    Runs the perceptron simulation and explains each deep learning concept.

    Args:
        custom_inputs (Optional[List[float]]): Optional preset inputs for testing.
        interactive (bool): Whether to prompt the user if inputs are not provided.

    Returns:
        str: Formatted educational report detailing the perceptron computation.
    """
    inputs: List[float] = []

    if custom_inputs is not None:
        inputs = [float(x) for x in custom_inputs[:3]]
    elif interactive:
        import sys
        if sys.stdin.isatty():
            print("Assistant: [Perceptron Demonstration]")
            print("Enter 3 numbers between -2.0 and 2.0 (e.g. 1.0, 0.5, -0.8)")
            try:
                raw = input("Enter inputs separated by spaces (or press Enter for default '1.0, 0.5, -0.8'): ").strip()
                if raw:
                    # Support comma or space separated numbers
                    tokens = raw.replace(",", " ").split()
                    for token in tokens[:3]:
                        inputs.append(float(token))
            except (ValueError, EOFError, KeyboardInterrupt):
                print("Assistant: Using standard default inputs.")
                inputs = []
        else:
            # Non-interactive / automated testing environment
            inputs = [1.0, 0.5, -0.8]

    # If fewer than 3 inputs provided, fill with defaults
    while len(inputs) < 3:
        inputs.append([1.0, 0.5, -0.8][len(inputs)])

    weights = DEFAULT_WEIGHTS
    bias = DEFAULT_BIAS

    res = calculate_neuron(inputs, weights, bias)

    calc_terms = " + ".join([f"({x} * {w})" for x, w in zip(inputs, weights)])
    report = (
        f"Assistant: --- Artificial Neuron (Perceptron) Forward Pass ---\n"
        f"  Inputs (x)         : {inputs}\n"
        f"  Weights (w)        : {weights}\n"
        f"  Bias (b)           : {bias}\n"
        f"  Formula            : z = sum(x_i * w_i) + b\n"
        f"  Calculation        : {calc_terms} + ({bias})\n"
        f"  Dot Product        : {res['dot_product']}\n"
        f"  Weighted Sum (z)   : {res['weighted_sum']}\n"
        f"  Activation Function: Step Function (output = 1 if z > 0 else 0)\n"
        f"  Final Output (y)   : {res['output']}\n"
        f"  {'-' * 55}\n"
        f"  [Deep Learning Concept Breakdown]\n"
        f"  1. Input: Numerical features representing observed data.\n"
        f"  2. Weight: Multipliers that amplify or inhibit specific inputs.\n"
        f"  3. Bias: An offset shifting the activation threshold.\n"
        f"  4. Forward Propagation: Left-to-right calculation from inputs to output.\n"
        f"  5. Note: This demo uses fixed handcrafted weights to illustrate neuron\n"
        f"     arithmetic. No actual gradient descent or parameter training occurred."
    )

    # Append optional hidden-layer analogy
    report += multi_layer_analogy(inputs)
    return report

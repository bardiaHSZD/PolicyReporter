import argparse
from src.threshold_optimizer import run_optimizer
from src.logger import logger

def parse_arguments():
    """
    Parses command-line arguments for the optimizer.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Threshold Optimizer")

    # Add arguments
    parser.add_argument(
        '--file_path', type=str, required=True,
        help="Path to the CSV file containing thresholds and classification results."
    )
    parser.add_argument(
        '--weights', type=float, nargs=4, metavar=('precision', 'recall', 'f1', 'fpr'),
        help="Weights for composite score calculation (precision, recall, F1, FPR). Provide exactly 4 weights."
    )

    return parser.parse_args()

def main():
    """
    Main entry point for running the Threshold Optimizer.
    """
    # Parse command-line arguments
    args = parse_arguments()

    # If weights are provided, convert to dictionary for composite score calculation
    weights = None
    if args.weights:
        if len(args.weights) != 4:
            logger.error("Please provide exactly 4 weights for composite score calculation: precision, recall, f1, and fpr.")
            return
        weights = {
            'precision': args.weights[0],
            'recall': args.weights[1],
            'f1': args.weights[2],
            'fpr': args.weights[3]
        }
        logger.info(f"Using weights for composite score: {weights}")

    # Run the optimizer
    result = run_optimizer(args.file_path, weights)

    if result:
        best_threshold = result["best_threshold"]
        logger.info(f"Best threshold selected: {best_threshold}")
        print(f"Best threshold selected: {best_threshold}")

if __name__ == '__main__':
    main()

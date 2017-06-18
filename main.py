import data_generation
import linearRegression

def main():
    # train model
    dataset = data_generation.create_label_with_points()
    linearRegression.createTrainedModel(dataset)

    linearRegression.predictMidpoint()
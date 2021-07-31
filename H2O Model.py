import h2o
import pandas as pd
from h2o.automl import H2OAutoML
import matplotlib.pyplot as plt

def H2oArchitecture(csv_path, SyntheticData_path):

    RealDataset = pd.read_csv(csv_path)
    RealDataset = RealDataset.drop("Unnamed: 0", axis=1)
    Real_training_dataset = RealDataset.sample(frac=0.8, random_state=25)
    Real_testing_dataset = RealDataset.drop(Real_training_dataset.index)
    discrete_columns = RealDataset.columns
    df_training = h2o.H2OFrame(Real_training_dataset)
    df_testing = h2o.H2OFrame(Real_testing_dataset)
    SyntheticData = pd.read_csv(SyntheticData_path)
    SyntheticData = SyntheticData.drop("Unnamed: 0", axis=1)
    df_syntheticData = h2o.H2OFrame(SyntheticData)
    print(df_syntheticData.head(10))

    discrete_columns = RealDataset.columns

    print(discrete_columns)
    print(df_training.head(10))
    print(len(Real_training_dataset.columns))

    print(df_testing.head(10))

    # def H2oSyntheticFrame(synthetic_path):
    # Synthetic_Data_Path = os.path.join('/' + 'content' + '/' + 'SyntheticData.csv')

    j = int(input())
    for j in range(4):
        if j > 0:
            # print(Real_training_dataset.columns)
            df_training_Barred = df_training[df_training.columns[j - 1]]
            x = df_training.columns
            y = df_training_Barred.columns[0]
            # print(df_training.head(10))
            print(x)
            print(y)

            aml = H2OAutoML(max_models=20, seed=1)
            aml.train(x=x, y=y, training_frame=df_training)

            print(aml.leaderboard)
            model_index = 0
            glm_index = 0
            glm_model = ''
            aml_leaderboard_df = aml.leaderboard.as_data_frame()
            models_dict = {}
            for m in aml_leaderboard_df['model_id']:
                models_dict[m] = model_index
                if 'StackedEnsemble' not in m:
                    break
                model_index = model_index + 1

            for m in aml_leaderboard_df['model_id']:
                if 'GLM' in m:
                    models_dict[m] = glm_index
                    break
                glm_index = glm_index + 1
            models_dict

            best_model = h2o.get_model(aml.leaderboard[model_index, 'model_id'])

            predictions = best_model.predict(df_testing)

            y_pred = h2o.as_list(predictions)
            print(y_pred[0:5])

            y_test = h2o.as_list(df_testing[df_testing.columns[j - 1]])
            print(y_test[0:5])

            plt.figure(figsize=(10, 5))
            plt.plot(y_pred, color='r', label=f"Predicted {y}")
            plt.plot(y_test, color='g', label=f"Actual {y}")
            plt.legend()
            plt.show()

            j += 1
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "language_models")

TEST_DIR = os.path.join(BASE_DIR, 'tests')
TEST_DATA_DIR = os.path.join(TEST_DIR, 'test_data')

MODEL = "stabilityai/stable-diffusion-xl-base-1.0" # general generative model
#MODEL = "cagliostrolab/animagine-xl-3.0" ## anime generator
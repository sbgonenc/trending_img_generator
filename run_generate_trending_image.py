
def execute(args):
    from lib.load_model import load_nn_model, generate_image
    from lib.get_trending_terms import get_trending_terms

    model = load_nn_model(args)

    for pop_term in get_trending_terms(args.country)[:args.n_trending_terms]:
        prompt = f"{pop_term} as {args.image_type}"
        for _ in range(args.n_images):
            img = generate_image(model, prompt)
            img.save(f"{args.out_dir}/{pop_term}_{_}.png")


if __name__ == "__main__":
    import argparse
    from config import MODEL
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", type=str, required=True)
    parser.add_argument("--n_trending_terms", type=str, required=False, default=10, help="Number of trending terms")
    parser.add_argument("--n_images", type=str, required=False, default=10, help="Number of images to generate per term")
    parser.add_argument("--image_type", type=str, required=False, default="caricature", help="generated image type")
    parser.add_argument("--out_dir", type=str, required=True, help="Output directory")
    parser.add_argument("--model", type=str, required=False, default=MODEL, help="Model name or path")
    args = parser.parse_args()
    execute(args)
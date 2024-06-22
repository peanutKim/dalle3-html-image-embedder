# dalle3-html-image-embedder GitHub Action

This action transform HTML comments into `<img>` elements with AI-generated images from DALL-E 3. The following is the syntax for the html comments:

```html
<!--image: your desired image prompt-->
```

Please refer to the example HTML within the testHTML folder.

## Quickstart

1. **Set Up OpenAI Secret Key**:

   - Go to your GitHub repository's Settings.
   - Navigate to "Secrets and variables" and select "New repository secret".
   - Name the secret `OPENAI_KEY` and paste your OpenAI secret key as the value.

2. **Configure the Workflow**:

   - In your repository, create a `.github/workflows` directory if it doesn't already exist.
   - Inside this directory, create a new file named `image-embedder.yml`.
   - Copy and paste the following workflow configuration into `image-embedder.yml`:

```yaml
name: image-embedder-action
on: [push, pull_request]

jobs:
  image-embedder:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: dalle3-image-embedder
        uses: peanutKim/dalle3-html-image-embedder@develop
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_KEY }}

      - name: Add generated images
        run: |
          git config --global user.email "actions@github.com"
          git config --global user.name "GitHub Actions Bot"
          git add .
          git commit -m ":art: added your ai generated images" || echo "No new images to commit."
          git push
```

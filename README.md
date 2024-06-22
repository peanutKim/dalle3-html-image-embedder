# dalle3-html-image-embedder GitHub Action

This action enables the automatic ai generation of `<img>` elements from HTML comments. For instance, a comment in an HTML file will be transformed into an `<img>` element, created by DALL-E 3 based on the specified prompt:

```html
<!--image: your desired image prompt-->
```

## Quickstart

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

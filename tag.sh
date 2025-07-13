export VERSION=v0.1.0

# 1. Update the file (search/replace version string)
#sed -i 's/^version = ".*"/version = "'"$VERSION"'"/' pyproject.toml

# 2. Stage it
git add pyproject.toml               # ← critical line

# 3. Commit & tag
git commit -m "chore(release): $VERSION"
git tag -a "$VERSION" -m "Release $VERSION"
git push origin main --follow-tags
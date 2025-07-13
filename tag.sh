export VERSION=v0.1.0

# 3. Commit & tag
git commit -m "chore(release): $VERSION"
git tag -a "$VERSION" -m "Release $VERSION"
git push origin main --follow-tags
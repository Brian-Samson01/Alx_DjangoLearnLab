
---

## 3️⃣ Update — `update.md`

```markdown
# Update Book

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

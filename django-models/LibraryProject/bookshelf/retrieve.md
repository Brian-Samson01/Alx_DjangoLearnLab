
---

## 2️⃣ Retrieve — `retrieve.md`

```markdown
# Retrieve Book

```python
Book.objects.all()

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year


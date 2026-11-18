import unittest, mdwiki, tempfile, pathlib
class T(unittest.TestCase):
    def test(self):
        d=pathlib.Path(tempfile.mkdtemp()); (d/"a.md").write_text("# Alfa\nveja [[b]]"); (d/"b.md").write_text("# Beta"); (d/"c.md").write_text("sem titulo")
        o=mdwiki.indexar(str(d)); self.assertIn("[[a]] Alfa (1 links)",o); self.assertIn("- a\n",o+"\n"); self.assertNotIn("- b\n",o+"\n")
unittest.main()

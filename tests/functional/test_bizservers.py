from daboserver.tests import *

class TestBizserversController(TestController):

    def test_index(self):
        response = self.app.get(url_for('bizservers'))
        # Test response...

    def test_index_as_xml(self):
        response = self.app.get(url_for('formatted_bizservers', format='xml'))

    def test_create(self):
        response = self.app.post(url_for('bizservers'))

    def test_new(self):
        response = self.app.get(url_for('new_bizserver'))

    def test_new_as_xml(self):
        response = self.app.get(url_for('formatted_new_bizserver', format='xml'))

    def test_update(self):
        response = self.app.put(url_for('bizserver', id=1))

    def test_update_browser_fakeout(self):
        response = self.app.post(url_for('bizserver', id=1), params=dict(_method='put'))

    def test_delete(self):
        response = self.app.delete(url_for('bizserver', id=1))

    def test_delete_browser_fakeout(self):
        response = self.app.post(url_for('bizserver', id=1), params=dict(_method='delete'))

    def test_show(self):
        response = self.app.get(url_for('bizserver', id=1))

    def test_show_as_xml(self):
        response = self.app.get(url_for('formatted_bizserver', id=1, format='xml'))

    def test_edit(self):
        response = self.app.get(url_for('edit_bizserver', id=1))

    def test_edit_as_xml(self):
        response = self.app.get(url_for('formatted_edit_bizserver', id=1, format='xml'))

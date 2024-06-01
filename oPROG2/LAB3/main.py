from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from dialog import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("QtWidget.ui", self)
        self.db = QSqlDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.mainModel = QSqlQueryModel()
        query_string = """SELECT
            f.id,
            f.title AS [Название],
            g.title AS [Жанр],
            f.year AS [Год выпуска],
            f.duration AS [Длительность]
        FROM films f 
        JOIN genres g on f.genre = g.id;"""
        self.mainModel.setQuery(query_string, self.db)

        self.tableView.setModel(self.mainModel)
        self.tableView.setColumnHidden(0, True)
        self.tableView.resizeColumnsToContents()
        self.tableView.doubleClicked.connect(self.doubleClick)

    def doubleClick(self, table):
        dialog = DialogForm()
        result = dialog.exec()

        if result == QDialog.Accepted:
            title = dialog.titleEdit.text()
            year = dialog.yearEdit.text()
            duration = dialog.durationEdit.text()

            errors = {
                "Error in film title": not title,
                "Error in film year": not year.isdigit(),
                "Error in film duration": not duration.isdigit(),
            }

            for error_message, condition in errors.items():
                if condition:
                    print(error_message)
                    return

            genre = dialog.genreBox.currentText()

            update_query = f"""UPDATE films
                SET title = '{title}',
                year = {int(year)},
                genre = (SELECT id FROM genres WHERE title = '{genre}'),
                duration = {int(duration)}
            WHERE id = {int(table.sibling(table.row(), 0).data())};"""

            query = QSqlQuery(self.db)
            if query.exec_(update_query):
                self.db.commit()
                query_string = """SELECT
                    f.id,
                    f.title AS [Название],
                    g.title AS [Жанр],
                    f.year AS [Год выпуска],
                    f.duration AS [Длительность]
                FROM films f 
                JOIN genres g on f.genre = g.id;"""
                self.mainModel.setQuery(query_string, self.db)
            else:
                print(query.lastError().text())


app = QApplication([])
window = MainForm()
window.show()
app.exec()

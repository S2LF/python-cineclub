from PySide2 import QtWidgets, QtCore
from movie import Movie, get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ciné Club')
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.qle = QtWidgets.QLineEdit()
        self.qlw = QtWidgets.QListWidget()
        self.qlw.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.qpb_add = QtWidgets.QPushButton('Ajouter un film')
        self.qpb_del = QtWidgets.QPushButton('Supprimer le(s) film(s)')

        self.layout.addWidget(self.qle)
        self.layout.addWidget(self.qpb_add)
        self.layout.addWidget(self.qlw)
        self.layout.addWidget(self.qpb_del)

    def addMovieToItem(self, movie):
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            # lw_item.setData(QtCore.Qt.UserRole, movie)
            lw_item.movie = movie
            self.qlw.addItem(lw_item)

    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            self.addMovieToItem(movie)


    def add_movie(self):
        movie = self.qle.text()
        if movie:
            movie = Movie(movie)
            added = movie.add_to_movies()
            if added:
                self.addMovieToItem(movie)
            self.qle.clear()
            self.qle.setFocus

    def remove_movie(self):
        for item in self.qlw.selectedItems():
            # movie = item.data(QtCore.Qt.UserRole)
            movie = item.movie
            movie.remove_from_movies()
            self.qlw.takeItem(self.qlw.row(item))

    def setup_connections(self):
        self.qpb_add.clicked.connect(self.add_movie)
        self.qle.returnPressed.connect(self.add_movie)
        self.qpb_del.clicked.connect(self.remove_movie)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
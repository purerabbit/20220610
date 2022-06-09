import string
import pymysql
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog, QMessageBox
from manager.book_design import Ui_book

#逻辑联系 操作数据库的一些函数
class book(QDialog):
    isAdd = False
    isRevise = False

    def __init__(self):
        QDialog.__init__(self)
        print('come here!')
        self.UI = Ui_book()
        self.UI.setupUi(self)
        self.UI.btn_comfirm.clicked.connect(lambda:self.addBook())

        # print(data[0][1]) # 打印第1行第2个数据, 也就是小明


    def getDatabase(self, val):
        self.db = val
        self.db.open()
        # print(self.db.open(),"book")
        self.isAdd=True

    def getOldBook(self,val,list):
        self.db=val
        self.isRevise=True
        self.db.open()
        # print(self.db.open(), "revise book")
        self.oldBookId=list[0]
        self.UI.line_bookId.setText(list[0])
        self.UI.line_bookName.setText(list[1])
        self.UI.line_author.setText(list[2])
        self.UI.line_bookNum.setText(list[3])


    def addBook(self):
        if self.isAdd:
            bookId = self.UI.line_bookId.text()
            bookName = self.UI.line_bookName.text()
            bookauthor = self.UI.line_author.text()
            bookNum = self.UI.line_bookNum.text()

            if len(bookId) is 0 or len(bookName) is 0 or len(bookauthor) is 0 or len(bookNum) is 0:
                QMessageBox.information(self, '提示', '信息填写不完整，请检查！', QMessageBox.Yes)
                return

            query = QSqlQuery()

            sql_addBook = "insert into book(bookId,bookName,author,bookNum) values(?,?,?,?)"
            query.prepare(sql_addBook)
            query.bindValue(0,bookId)
            query.bindValue(1,bookName)
            query.bindValue(2,bookauthor)
            query.bindValue(3,bookNum)

            if query.exec_():
                self.close()
                QMessageBox.information(self, '提示', '添加书本成功', QMessageBox.Yes)
            else:
                QMessageBox.information(self, '提示', '添加失败，可能编号已被添加或信息有误', QMessageBox.Yes)

        if self.isRevise:
            newBookId = self.UI.line_bookId.text()
            newBookName = self.UI.line_bookName.text()
            newBookAuthor = self.UI.line_author.text()
            newBookNum = self.UI.line_bookNum.text()

            if len(newBookId) is 0 or len(newBookName) is 0 or len(newBookAuthor) is 0 or len(newBookNum) is 0:
                QMessageBox.information(self, '提示', '修改失败，信息不能为空，请检查', QMessageBox.Yes)
            else:
                query = QSqlQuery()
                sql_updateBook = "update book set bookId=?,bookName=?,author=?,bookNum=? where bookId=?"

                query.prepare(sql_updateBook)
                query.bindValue(0,newBookId)
                query.bindValue(1,newBookName)
                query.bindValue(2,newBookAuthor)
                query.bindValue(3,newBookNum)
                query.bindValue(4,self.oldBookId)

                if query.exec_():
                    self.close()
                    QMessageBox.information(self, '提示', '修改成功！', QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '提示', '修改失败，可能该编号已存在', QMessageBox.Yes)



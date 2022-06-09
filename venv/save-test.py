# 數據庫設置 讀取數據庫內容
def Table_Data(self, i, j, data1):
    print(11111)
    _translate = QtCore.QCoreApplication.translate
    print(1)
    item = QtWidgets.QTableWidgetItem()
    print(2)
    self.tableView.setItem(i, j, item)
    print(3)
    item = self.tableView.item(i, j)
    print(4)
    # MdiArea.setWindowTitle(_translate("MdiArea", "MdiArea"))
    item.setText(_translate("MdiArea", str(data1)))  #############
    print(5)


def reviseBook(self):
    # print('jinrule reviseBook!!!')
    _translate = QtCore.QCoreApplication.translate
    total = self.cursor.execute(
        "select id, username, userpassword, identity  from user").fetchall()
    self.vol = 4
    self.row = 8
    self.tableView.setColumnCount(self.vol)
    self.tableView.setRowCount(self.row)

    total = list(total)  # 将数据格式改为列表形式，其是将数据库中取出的数据整体改为列表形式
    for i in range(len(total)):  # 将相关的数据
        total[i] = list(total[i])  # 将获取的数据转为列表形式

    a = 0
    item = QtWidgets.QTableWidgetItem()
    self.tableView.setHorizontalHeaderItem(a, item)
    item = self.tableView.horizontalHeaderItem(a)
    # item.setText("ID")
    item.setText(_translate("MdiArea", "ID"))

    a = 1
    item = QtWidgets.QTableWidgetItem()
    self.tableView.setHorizontalHeaderItem(a, item)
    item = self.tableView.horizontalHeaderItem(a)
    # item.setText("name")
    item.setText(_translate("MdiArea", "name"))
    a = 2
    item = QtWidgets.QTableWidgetItem()
    self.tableView.setHorizontalHeaderItem(a, item)
    item = self.tableView.horizontalHeaderItem(a)
    # item.setText("password")
    item.setText(_translate("MdiArea", "password"))

    a = 3
    item = QtWidgets.QTableWidgetItem()
    self.tableView.setHorizontalHeaderItem(a, item)
    item = self.tableView.horizontalHeaderItem(a)
    # item.setText("identity")
    item.setText(_translate("MdiArea", "identity"))

    for i in range(self.row):
        for j in range(self.vol):
            print('total[i][j]:', total[i][j])
            self.Table_Data(i, j, total[i][j])


def showcontent(self, data):
    shrow = len(data)  # 取得记录个数，用于设置表格的行数
    shvol = len(data[0])  # 取得字段数，用于设置表格的列数
    for i in range(shrow):
        for j in range(shvol):
            print("进来啦！")
            print("i:", i)
            print("j:", j)
            print('data[i][j]:', data[i][j])
            self.Table_Data(i, j, data[i][j])


# 查找书本
def searchBook(self):
    print('come into searchBook')
    index = self.comboBox.currentIndex()
    print('comboBox is ok')
    searchText = self.line_context.text()
    # if len(searchText) == 0:
    #     QMessageBox.information(self, '提示', '请输入要搜索的内容！', QMessageBox.Yes)#没有输入时的提示
    #     return
    sql_searchAll = "select id, username, userpassword, identity  from user"
    sql_searchBookId = "select id, username, userpassword, identity  from user where id =?"
    # sql_searchBookId = "select id, username, userpassword, identity  from user where id =?"
    sql_searchBookName = "select id, username, userpassword, identity  from user where username =?"
    sql_searchBookAuthor = "select id, username, userpassword, identity  from user where identity =?"
    print("index:", index)
    print("searchText:", searchText)
    # 接下来是将数据显示到组件中
    if index == 1:
        self.cursor.execute(sql_searchAll)
        data = self.cursor.fetchall()
        print("data1:", data)

    if index == 2:
        self.cursor.execute(sql_searchBookId, [searchText])  # 根据id进行查找
        data = self.cursor.fetchall()
        self.showcontent(data)
        print("data2:", data)
    if index == 3:
        self.cursor.execute(sql_searchBookName, [searchText])  # 根据用户名进行查找
        data = self.cursor.fetchall()
        print("data3:", data)
    if index == 4:
        self.cursor.execute(sql_searchBookAuthor, [searchText])  # 根据身份进行查找
        data = self.cursor.fetchall()
        print("data4:", data)

    if data != "":
        _translate = QtCore.QCoreApplication.translate
        item = QtWidgets.QTableWidgetItem()
        i = 0
        col = 4
        for j in range(col):
            self.tableView.setItem(i, j, item)
            item = self.tableView.item(i, j)
            # MdiArea.setWindowTitle(_translate("MdiArea", "MdiArea"))
            item.setText(_translate("MdiArea", str(data[j])))  #############



        # if query.next():
        #
        #     self.model.clear()
        #     self.model.setColumnCount(4)
        #     self.model.setHorizontalHeaderLabels(['编号', '书名', '作者', '库存'])
        #
        #     for column in range(4):
        #         item = QStandardItem("%s" % (query.value(column)))
        #         # 设置每个位置的文本值
        #         self.model.setItem(0, column, item)
        #
        #     row = 1
        #
        #     while query.next():
        #         for column in range(4):
        #             item = QStandardItem("%s" % (query.value(column)))
        #             # 设置每个位置的文本值
        #             self.model.setItem(row, column, item)
        #         row = row + 1

        else:
            QMessageBox.information(self, '提示', '查询不到内容！', QMessageBox.Yes)


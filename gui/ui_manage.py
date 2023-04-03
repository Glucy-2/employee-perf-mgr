# -*- coding: utf-8 -*-

import os
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import account
import file
from staff import Staff
from gui import msgbox


class Window(QDialog):
    def __init__(self):
        super().__init__()

        # 加载ui文件
        qfile = QFile(f"{os.path.abspath('.')}/gui/manage.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 创建ui窗口对象
        self.ui = QUiLoader().load(qfile)

        # 提取要操作的控件

        # “文件”组
        self.readfile_btn = self.ui.readfile_btn  # 读取按钮
        self.savefile_btn = self.ui.savefile_btn  # 保存按钮

        # “排序”组
        self.sort_ref_combobox = self.ui.sort_ref_combobox  # 排序参考下拉框
        self.sort_mode_combobox = self.ui.sort_mode_combobox  # 排序顺序下拉框
        self.sort_enter_btn = self.ui.sort_enter_btn  # 应用按钮

        # “添加/修改数据”组
        self.mode_add_radiobtn = self.ui.mode_add_radiobtn  # 添加模式单选按钮
        self.mode_edit_radiobtn = self.ui.mode_edit_radiobtn  # 修改模式单选按钮
        self.id_edit = self.ui.id_edit  # 工号编辑框
        self.name_edit = self.ui.name_edit  # 姓名编辑框
        self.male_radiobtn = self.ui.male_radiobtn  # 男性单选按钮
        self.female_radiobtn = self.ui.female_radiobtn  # 女性单选按钮
        self.quarter1_perf_spinbox = (
            self.ui.quarter1_perf_spinbox
        )  # 第一季度业绩编辑框
        self.quarter2_perf_spinbox = (
            self.ui.quarter2_perf_spinbox
        )  # 第二季度业绩编辑框
        self.quarter3_perf_spinbox = (
            self.ui.quarter3_perf_spinbox
        )  # 第三季度业绩编辑框
        self.quarter4_perf_spinbox = (
            self.ui.quarter4_perf_spinbox
        )  # 第四季度业绩编辑框
        self.all_perf_edit = self.ui.all_perf_edit  # 总业绩编辑框
        self.all_perf_rank_edit = self.ui.all_perf_rank_edit  # 总业绩排名编辑框
        self.edit_enter_btn = self.ui.edit_enter_btn  # 确定按钮
        self.edit_del_btn = self.ui.edit_del_btn  # 删除员工按钮
        self.edit_cancel_btn = self.ui.edit_cancel_btn  # 取消按钮

        # “搜索查询查询”组
        self.id_search_edit = self.ui.id_search_edit  # 工号搜索框
        self.quarter_select_combobox = self.ui.quarter_select_combobox  # 季度下拉框
        self.search_id_btn = self.ui.search_id_btn  # 按工号搜索按钮
        self.query_quarter_btn = self.ui.query_quarter_btn  # 按季度查询按钮

        # 主表格
        self.main_table = self.ui.main_table  # 表格
        self.main_table.setEditTriggers(QTableWidget.NoEditTriggers)  # 设置表格不可编辑

        # 绑定信号与槽函数
        self.readfile_btn.clicked.connect(self.read)  # 读取文件按钮
        self.savefile_btn.clicked.connect(self.save)  # 保存文件按钮
        self.sort_enter_btn.clicked.connect(self.sort_enter)  # 排序应用按钮
        self.edit_enter_btn.clicked.connect(self.edit_enter)  # 编辑确定按钮
        self.edit_del_btn.clicked.connect(self.edit_del)  # 编辑删除按钮
        self.edit_cancel_btn.clicked.connect(self.edit_cancel)  # 编辑取消按钮
        self.search_id_btn.clicked.connect(self.search_id)  # 按工号搜索按钮
        self.query_quarter_btn.clicked.connect(self.query_quarter)  # 按季度查询按钮
        self.main_table.itemSelectionChanged.connect(self.table_select)  # 表格选中项改变时触发
        self.quarter1_perf_spinbox.valueChanged.connect(
            self.quater_changed
        )  # 业绩编辑框内容改变时触发
        self.quarter2_perf_spinbox.valueChanged.connect(
            self.quater_changed
        )  # 业绩编辑框内容改变时触发
        self.quarter3_perf_spinbox.valueChanged.connect(
            self.quater_changed
        )  # 业绩编辑框内容改变时触发
        self.quarter4_perf_spinbox.valueChanged.connect(
            self.quater_changed
        )  # 业绩编辑框内容改变时触发

    def update(self):  # 读取变量写表格
        self.main_table.setHorizontalHeaderLabels(
            [
                "工号",
                "姓名",
                "性别",
                "第一季度的业绩",
                "第二季度的业绩",
                "第三季度的业绩",
                "第四季度的业绩",
                "总业绩",
                "总业绩排名",
            ]
        )  # 设置表头文字
        self.main_table.setRowCount(len(self.staff_list))  # 设置表格行数
        row = 0  # 行号
        for one_staff in self.staff_list:  # 逐条写入数据到表格
            self.main_table.setItem(row, 0, QTableWidgetItem(one_staff.getNum()))
            self.main_table.setItem(row, 1, QTableWidgetItem(one_staff.getName()))
            if one_staff.getGender() == "Male":
                self.main_table.setItem(row, 2, QTableWidgetItem("男"))
            elif one_staff.getGender() == "Female":
                self.main_table.setItem(row, 2, QTableWidgetItem("女"))
            else:
                self.main_table.setItem(row, 2, QTableWidgetItem("未知"))
            self.main_table.setItem(
                row, 3, QTableWidgetItem(str(one_staff.getScore()[1]))
            )
            self.main_table.setItem(
                row, 4, QTableWidgetItem(str(one_staff.getScore()[2]))
            )
            self.main_table.setItem(
                row, 5, QTableWidgetItem(str(one_staff.getScore()[3]))
            )
            self.main_table.setItem(
                row, 6, QTableWidgetItem(str(one_staff.getScore()[4]))
            )
            self.main_table.setItem(row, 7, QTableWidgetItem(str(one_staff.getTotal())))
            self.main_table.setItem(row, 8, QTableWidgetItem(str(one_staff.getRank())))
            row += 1

    def read(self):
        self.staff_list = []  # 清空员工列表
        all_num = file.read_file(self.staff_list)  # 读取文件
        if all_num:
            self.update()
            self.sort_ref_combobox.setCurrentIndex(0)  # 重置排序参考下拉框
            self.sort_ref_combobox.addItem("工号")
            self.sort_ref_combobox.addItem("姓名")
            self.sort_ref_combobox.addItem("第一季度业绩")
            self.sort_ref_combobox.addItem("第二季度业绩")
            self.sort_ref_combobox.addItem("第三季度业绩")
            self.sort_ref_combobox.addItem("第四季度业绩")
            self.sort_ref_combobox.addItem("总业绩")
            self.sort_ref_combobox.addItem("总业绩排名")
            self.sort_mode_combobox.setCurrentIndex(0)  # 重置排序顺序下拉框
            self.sort_mode_combobox.addItem("升序")
            self.sort_mode_combobox.addItem("降序")
            self.quarter_select_combobox.setCurrentIndex(0)  # 重置季度选择下拉框
            self.quarter_select_combobox.addItem("第一季度")
            self.quarter_select_combobox.addItem("第二季度")
            self.quarter_select_combobox.addItem("第三季度")
            self.quarter_select_combobox.addItem("第四季度")
            self.quarter_select_combobox.addItem("总业绩")
            msgbox.info(
                "读取成功",
                f"成功读取 {len(self.staff_list)} 条数据\n修改数据请在左侧修改，表格不可修改但自动更新\n修改后记得保存",
            )
            self.main_table.resizeColumnsToContents()  # 自动调整列宽
            self.main_table.resizeRowsToContents()  # 自动调整行高
        else:
            msgbox.error("读取失败", "文件不存在或文件内容为空或者错误")

    def save(self):
        result = file.save_file(self.staff_list)
        if result is None:  # 没出错（出错了会由file.save_file自己弹窗）
            msgbox.info("保存成功", f"成功保存 {len(self.staff_list)} 条数据")

    def sort_by_id(self, one_staff):
        return one_staff.getNum()

    def sort_by_name(self, one_staff):
        return one_staff.getName()

    def sort_by_quarter1(self, one_staff):
        return int(one_staff.getScore()[1])

    def sort_by_quarter2(self, one_staff):
        return int(one_staff.getScore()[2])

    def sort_by_quarter3(self, one_staff):
        return int(one_staff.getScore()[3])

    def sort_by_quarter4(self, one_staff):
        return int(one_staff.getScore()[4])

    def sort_by_total(self, one_staff):
        return int(one_staff.getTotal())

    def sort_by_rank(self, one_staff):
        return int(one_staff.getRank())

    def sort_enter(self):
        ref = self.sort_ref_combobox.currentText()
        if ref == "工号":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_id,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "姓名":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_name,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第一季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_quarter1,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第二季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_quarter2,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第三季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_quarter3,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第四季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_quarter4,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "总业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_total,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "总业绩排名":
            self.staff_list = sorted(
                self.staff_list,
                key=self.sort_by_rank,
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        else:
            msgbox.error("排序错误", "排序参考选择错误，是否已经读取文件？")
            return
        self.update()

    def edit_enter(self):
        if self.mode_add_radiobtn.isChecked():
            for one_staff in self.staff_list:
                if one_staff.getNum() == self.id_edit.text():
                    msgbox.error("添加错误", "该工号已存在")
                    return
            else:
                if self.male_radiobtn.isChecked():
                    gender = "Male"
                elif self.female_radiobtn.isChecked():
                    gender = "Female"
                else:
                    msgbox.error("添加失败", "性别选择错误")
                    return
                self.staff_list.append(
                    Staff(
                        self.id_edit.text(),
                        self.name_edit.text(),
                        gender,
                        {
                            1: self.quarter1_perf_spinbox.value(),
                            2: self.quarter2_perf_spinbox.value(),
                            3: self.quarter3_perf_spinbox.value(),
                            4: self.quarter4_perf_spinbox.value(),
                        },
                        self.quarter1_perf_spinbox.value()
                        + self.quarter2_perf_spinbox.value()
                        + self.quarter3_perf_spinbox.value()
                        + self.quarter4_perf_spinbox.value(),
                        "",
                    )
                )
                self.staff_list = sorted(
                    self.staff_list, key=self.sort_by_total, reverse=True
                )
                rank = 1
                for one_sta in self.staff_list:
                    one_sta.setRank(str(rank))
                    rank += 1
                self.sort_enter()
                msgbox.info("添加成功", "表格已刷新")
        elif self.mode_edit_radiobtn.isChecked():
            for one_staff in self.staff_list:
                if one_staff.getNum() == self.id_edit.text():
                    if self.male_radiobtn.isChecked():
                        gender = "Male"
                    elif self.female_radiobtn.isChecked():
                        gender = "Female"
                    else:
                        msgbox.error("添加错误", "性别选择错误")
                    one_staff.setName(self.name_edit.text())
                    one_staff.setGender(gender)
                    one_staff.setScore(
                        {
                            1: self.quarter1_perf_spinbox.value(),
                            2: self.quarter2_perf_spinbox.value(),
                            3: self.quarter3_perf_spinbox.value(),
                            4: self.quarter4_perf_spinbox.value(),
                        }
                    )
                    one_staff.setTotal(
                        self.quarter1_perf_spinbox.value()
                        + self.quarter2_perf_spinbox.value()
                        + self.quarter3_perf_spinbox.value()
                        + self.quarter4_perf_spinbox.value()
                    )
                    self.staff_list = sorted(
                        self.staff_list, key=self.sort_by_total, reverse=True
                    )
                    rank = 1
                    for one_sta in self.staff_list:
                        one_sta.setRank(str(rank))
                        rank += 1
                    self.sort_enter()
                    msgbox.info("修改成功", "表格已刷新")
                    break
                else:
                    print(self.id_edit.text())
            else:
                msgbox.error("修改错误", "该工号不存在，请检查模式是否正确")
                return
        else:
            msgbox.error("错误", "请选择添加/修改模式")

    def edit_del(self):
        if self.id_edit.text() == "":
            msgbox.error("错误", "请输入工号")
            return
        else:
            for sta in self.staff_list:  # 寻找待删除的元素
                if sta.getNum() == self.id_edit.text():  # 如果找到相等元素
                    self.staff_list.remove(sta)  # 删除对应的元素
                    self.update()
                    msgbox.info("删除成功", "表格已刷新")
                    break
            else:
                msgbox.error("删除错误", "该工号不存在")
                return

    def edit_cancel(self):
        self.table_select()

    def search_id(self):
        ref = self.id_search_edit.text()
        if ref == "":
            msgbox.error("查询错误", "请输入工号")
            return
        else:
            for one_staff in self.staff_list:
                if one_staff.getNum() == ref:
                    self.table_select()
                    self.main_table.selectRow(list(self.staff_list).index(one_staff))
                    msgbox.info("查询成功", "已选中该员工所在行")
                    return
            else:
                msgbox.error("查询错误", "该工号不存在")
            return

    def query_quarter(self):
        ref = self.quarter_select_combobox.currentText()
        quater_perf = []
        try:
            if ref == "第一季度":
                for one_staff in self.staff_list:
                    quater_perf.append(int(one_staff.getScore()[1]))
            elif ref == "第二季度":
                for one_staff in self.staff_list:
                    quater_perf.append(int(one_staff.getScore()[2]))
            elif ref == "第三季度":
                for one_staff in self.staff_list:
                    quater_perf.append(int(one_staff.getScore()[3]))
            elif ref == "第四季度":
                for one_staff in self.staff_list:
                    quater_perf.append(int(one_staff.getScore()[4]))
            elif ref == "总业绩":
                for one_staff in self.staff_list:
                    quater_perf.append(int(one_staff.getTotal()))
            else:
                msgbox.error("查询错误", "季度选择错误，是否已经读取文件？")
                return
        except ValueError:
            msgbox.error("查询错误", "业绩数据格式错误，请检查业绩是否均为整数")
            return
        msgbox.info(
            "查询结果",
            f"{ref}：\n平均业绩：{sum(quater_perf)/len(quater_perf)}\n最高业绩：{max(quater_perf)}\n最低业绩：{min(quater_perf)}",
        )

    def table_select(self):
        if self.mode_edit_radiobtn.isChecked():
            selected_items = self.main_table.selectedItems()  # 获取选中的单元格列表
            if selected_items:
                row = selected_items[0].row()  # 获取选中的单元格的第一行
                self.id_edit.setText(self.main_table.item(row, 0).text())
                self.name_edit.setText(self.main_table.item(row, 1).text())
                if self.main_table.item(row, 2).text() == "男":
                    self.male_radiobtn.setChecked(True)
                    self.female_radiobtn.setChecked(False)
                elif self.main_table.item(row, 2).text() == "女":
                    self.male_radiobtn.setChecked(False)
                    self.female_radiobtn.setChecked(True)
                else:
                    msgbox.error(
                        "性别错误",
                        f"性别数据错误，表格中 {self.main_table.item(row, 0).text()} 的性别数据是否正确（男/女）？",
                    )
                self.quarter1_perf_spinbox.setValue(
                    int(self.main_table.item(row, 3).text())
                )
                self.quarter2_perf_spinbox.setValue(
                    int(self.main_table.item(row, 4).text())
                )
                self.quarter3_perf_spinbox.setValue(
                    int(self.main_table.item(row, 5).text())
                )
                self.quarter4_perf_spinbox.setValue(
                    int(self.main_table.item(row, 6).text())
                )
                self.all_perf_edit.setText(self.main_table.item(row, 7).text())
                self.all_perf_rank_edit.setText(self.main_table.item(row, 8).text())

    def quater_changed(self):
        self.all_perf_edit.setText("添加或修改后计算")
        self.all_perf_rank_edit.setText("添加或修改后计算")

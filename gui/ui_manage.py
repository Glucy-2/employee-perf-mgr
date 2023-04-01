# -*- coding: utf-8 -*-

import os
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import account
import staff
from gui import msgbox
from gui import ui_manage


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
        self.quarter1_perf_edit = self.ui.quarter1_perf_edit  # 第一季度业绩编辑框
        self.quarter2_perf_edit = self.ui.quarter2_perf_edit  # 第二季度业绩编辑框
        self.quarter3_perf_edit = self.ui.quarter3_perf_edit  # 第三季度业绩编辑框
        self.quarter4_perf_edit = self.ui.quarter4_perf_edit  # 第四季度业绩编辑框
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
        self.quarter1_perf_edit.textChanged.connect(self.quater_changed)  # 业绩编辑框内容改变时触发

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
        for per_staff in self.staff_list:  # 逐条写入数据到表格
            self.main_table.setItem(row, 0, QTableWidgetItem(per_staff[0]))
            self.main_table.setItem(row, 1, QTableWidgetItem(per_staff[1]["name"]))
            if per_staff[1]["gender"] == "Male":
                self.main_table.setItem(row, 2, QTableWidgetItem("男"))
            elif per_staff[1]["gender"] == "Female":
                self.main_table.setItem(row, 2, QTableWidgetItem("女"))
            else:
                self.main_table.setItem(row, 2, QTableWidgetItem("未知"))
            self.main_table.setItem(row, 3, QTableWidgetItem(per_staff[1]["quarter1"]))
            self.main_table.setItem(row, 4, QTableWidgetItem(per_staff[1]["quarter2"]))
            self.main_table.setItem(row, 5, QTableWidgetItem(per_staff[1]["quarter3"]))
            self.main_table.setItem(row, 6, QTableWidgetItem(per_staff[1]["quarter4"]))
            self.main_table.setItem(row, 7, QTableWidgetItem(per_staff[1]["total"]))
            self.main_table.setItem(row, 8, QTableWidgetItem(str(per_staff[1]["rank"])))
            row += 1

    def read(self):
        read_data = staff.read_file()
        self.staff_list = read_data.items()
        if self.staff_list:  # 未出错（如果出错会由staff模块弹窗）
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
            msgbox.info("读取成功", f"成功读取 {len(self.staff_list)} 条数据\n修改数据请在左侧修改，表格不可修改但自动更新\n修改后记得保存")

    def save(self):
        save_data = {}
        for item in self.staff_list:
            save_data[item[0]] = item[1]
        result = staff.save_file(save_data)
        if result:  # 出错
            msgbox.error("保存失败", f"详细信息：{result}")
        else:
            msgbox.info("保存成功", f"成功保存 {len(self.staff_list)} 条数据")

    def sort_enter(self):
        ref = self.sort_ref_combobox.currentText()
        if ref == "工号":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[0],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "姓名":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["name"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第一季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["quarter1"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第二季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["quarter2"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第三季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["quarter3"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "第四季度业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["quarter4"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "总业绩":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["total"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        elif ref == "总业绩排名":
            self.staff_list = sorted(
                self.staff_list,
                key=lambda x: x[1]["rank"],
                reverse=True
                if self.sort_mode_combobox.currentText() == "降序"
                else False,
            )
        else:
            msgbox.error("排序错误", "排序参考选择错误，是否已经读取文件？")
            return
        self.update()

    def edit_enter(self):
        # staff_list先转换成字典
        staff_data = {}
        for item in self.staff_list:
            staff_data[item[0]] = item[1]
        if self.mode_add_radiobtn.isChecked():
            if self.id_edit.text() in list(staff_data.keys()):
                msgbox.error("添加错误", "该工号已存在")
                return
            else:
                if self.male_radiobtn.isChecked():
                    gender = "Male"
                elif self.female_radiobtn.isChecked():
                    gender = "Female"
                else:
                    msgbox.error("添加错误", "性别选择错误")
                staff_data[self.id_edit.text()] = {
                    "name": self.name_edit.text(),
                    "gender": gender,
                    "quarter1": self.quarter1_perf_edit.text(),
                    "quarter2": self.quarter2_perf_edit.text(),
                    "quarter3": self.quarter3_perf_edit.text(),
                    "quarter4": self.quarter4_perf_edit.text(),
                    "total": str(
                        int(self.quarter1_perf_edit.text())
                        + int(self.quarter2_perf_edit.text())
                        + int(self.quarter3_perf_edit.text())
                        + int(self.quarter4_perf_edit.text())
                    ),
                    "rank": "",
                }
                self.staff_list = staff_data.items()
                self.staff_list = sorted(self.staff_list, key=lambda x: x[1]["total"], reverse=True)
                for i in range(len(self.staff_list)):
                    self.staff_list[i][1]["rank"] = str(i + 1)
                self.staff_list = staff_data.items()
                self.sort_enter()
                msgbox.info("添加成功", "表格已刷新")
        elif self.mode_edit_radiobtn.isChecked():
            if self.id_edit.text() not in list(staff_data.keys()):
                msgbox.error("修改错误", "该工号不存在，请检查模式是否正确")
                return
            if self.male_radiobtn.isChecked():
                gender = "Male"
            elif self.female_radiobtn.isChecked():
                gender = "Female"
            else:
                msgbox.error("添加错误", "性别选择错误")

            staff_data[self.id_edit.text()] = {
                "name": self.name_edit.text(),
                "gender": gender,
                "quarter1": self.quarter1_perf_edit.text(),
                "quarter2": self.quarter2_perf_edit.text(),
                "quarter3": self.quarter3_perf_edit.text(),
                "quarter4": self.quarter4_perf_edit.text(),
                "total": str(
                    int(self.quarter1_perf_edit.text())
                    + int(self.quarter2_perf_edit.text())
                    + int(self.quarter3_perf_edit.text())
                    + int(self.quarter4_perf_edit.text())
                ),
                "rank": "",
            }
            self.staff_list = staff_data.items()
            self.staff_list = sorted(self.staff_list, key=lambda x: x[1]["total"], reverse=True)
            for i in range(len(self.staff_list)):
                self.staff_list[i][1]["rank"] = str(i + 1)
            self.staff_list = staff_data.items()
            self.sort_enter()
            msgbox.info("修改成功", "表格已刷新")
        else:
            msgbox.error("错误", "请选择添加/修改模式")

    def edit_del(self):
        if self.id_edit.text() == "":
            msgbox.error("错误", "请输入工号")
            return
        else:
            staff_data = {}
            for item in self.staff_list:
                staff_data[item[0]] = item[1]
            if self.id_edit.text() in staff_data:
                staff_data.pop(self.id_edit.text())
                self.staff_list = staff_data.items()
                self.update()
                msgbox.info("删除成功", "表格已刷新")
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
            for per_staff in self.staff_list:
                if per_staff[0] == ref:
                    self.table_select()
                    self.main_table.selectRow(list(self.staff_list).index(per_staff))
                    msgbox.info("查询成功", "已选中该员工所在行")
                    return
            msgbox.error("查询错误", "该工号不存在")
            return

    def query_quarter(self):
        staff_data = {}
        for item in self.staff_list:
            staff_data[item[0]] = item[1]
        ref = self.quarter_select_combobox.currentText()
        quater_perf = []
        try:
            if ref == "第一季度":
                for per_staff in staff_data:
                    quater_perf.append(int(staff_data[per_staff]["quarter1"]))
            elif ref == "第二季度":
                for per_staff in staff_data:
                    quater_perf.append(int(staff_data[per_staff]["quarter2"]))
            elif ref == "第三季度":
                for per_staff in staff_data:
                    quater_perf.append(int(staff_data[per_staff]["quarter3"]))
            elif ref == "第四季度":
                for per_staff in staff_data:
                    quater_perf.append(int(staff_data[per_staff]["quarter4"]))
            elif ref == "总业绩":
                for per_staff in staff_data:
                    quater_perf.append(int(staff_data[per_staff]["total"]))
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
                self.quarter1_perf_edit.setText(self.main_table.item(row, 3).text())
                self.quarter2_perf_edit.setText(self.main_table.item(row, 4).text())
                self.quarter3_perf_edit.setText(self.main_table.item(row, 5).text())
                self.quarter4_perf_edit.setText(self.main_table.item(row, 6).text())
                self.all_perf_edit.setText(self.main_table.item(row, 7).text())
                self.all_perf_rank_edit.setText(self.main_table.item(row, 8).text())

    def quater_changed(self):
        if (
            self.quarter1_perf_edit
            and self.quarter2_perf_edit
            and self.quarter3_perf_edit
            and self.quarter4_perf_edit
        ):
            self.all_perf_edit.setText("添加或修改后计算")
            self.all_perf_rank_edit.setText("添加或修改后计算")

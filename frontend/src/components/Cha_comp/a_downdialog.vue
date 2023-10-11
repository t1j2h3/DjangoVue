<template>
  <el-col :span="4"
    ><el-button @click="addDialogVisible = true" type="primary"
      >导出全部信息</el-button
    >
    <!-- 导出全部信息对话框 -->
    <el-dialog
      title="导出全部信息"
      :visible.sync="addDialogVisible"
      width="60%"
      @close="addDialogClosed"
      :modal-append-to-body="false"
    >
      <!-- 导出全部信息主体区域 -->
      <el-checkbox
        :indeterminate="isIndeterminate"
        v-model="checkAll"
        @change="handleCheckAllChange"
        >全选</el-checkbox
      >
      <div style="margin: 15px 0"></div>
      <el-checkbox-group
        v-model="checkedfields"
        @change="handlecheckedfieldsChange"
      >
        <el-checkbox
          v-for="(field, index) in fields"
          :label="field"
          :key="index"
          style="width: 160px"
          >{{ field.Chinese }}</el-checkbox
        >
      </el-checkbox-group>
      <!-- 导出全部信息信息底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="downmessage">确 定</el-button>
      </span>
    </el-dialog>
  </el-col>
</template>

<script>
const fieldOptions = [
  {
    id: 1,
    Chinese: "所处发展阶段",
    English: "status",
  },
  { id: 2, Chinese: "性别", English: "gender" },
  { id: 3, Chinese: "电话", English: "phone" },
  {
    id: 4,
    Chinese: "班级",
    English: "classx",
  },
  {
    id: 5,
    Chinese: "身份证",
    English: "identity_card",
  },
  {
    id: 6,
    Chinese: "民族",
    English: "nation",
  },
  { id: 7, Chinese: "籍贯", English: "native" },
  { id: 8, Chinese: "所在学院", English: "college" },
  { id: 9, Chinese: "所在支部", English: "branch" },
  { id: 10, Chinese: "出生日期", English: "birth_date" },
  { id: 11, Chinese: "首次提交申请书时间", English: "First_application" },
  { id: 12, Chinese: "首次申请入党学期", English: "semester" },
  { id: 13, Chinese: "党组织谈话时间", English: "talking_date" },
  { id: 14, Chinese: "党组织谈话人", English: "talker" },
  { id: 15, Chinese: "列为入党积极分子时间", English: "activists_date" },
  {
    id: 16,
    Chinese: "入党积极分子培训班情况",
    English: "courses_for_activists",
  },
  {
    id: 17,
    Chinese: "入党积极分子培训班结业时间",
    English: "activists_graduation",
  },
  { id: 18, Chinese: "入党积极培训班成绩", English: "activists_grade" },
  { id: 19, Chinese: "入党积极分子评优情况", English: "activists_appraising" },
  { id: 20, Chinese: "入党积极培训班情况备注", English: "activists_remarks" },
  { id: 21, Chinese: "培养联系人1", English: "contacts1" },
  { id: 22, Chinese: "培养联系人2", English: "contacts2" },
  {
    id: 23,
    Chinese: "积极分子考察登记表是否上传",
    English: "investigation_registration",
  },
  { id: 24, Chinese: "列为发展对象的时间", English: "developer_date" },
  { id: 25, Chinese: "发展对象培训班情况", English: "courses_for_developer" },
  {
    id: 26,
    Chinese: "发展对象培训班结业时间",
    English: "developer_graduation",
  },
  { id: 27, Chinese: "发展对象培训班成绩", English: "developer_grade" },
  { id: 28, Chinese: "发展对象评优情况", English: "developer_appraising" },
  { id: 29, Chinese: "发展对象培训班情况备注", English: "developer_remarks" },
  { id: 30, Chinese: "入党介绍人1", English: "introducer1" },
  { id: 31, Chinese: "入党介绍人2", English: "introducer2" },
  { id: 32, Chinese: "群众座谈人员名单是否上传", English: "mass_discussion" },
  { id: 33, Chinese: "列为预备党员的时间", English: "probation_date" },
  { id: 34, Chinese: "预备党员情况备注", English: "probation_remarks" },
  { id: 35, Chinese: "入党志愿书编号", English: "number" },
  { id: 36, Chinese: "转为正式党员日期", English: "formal_date" },
  { id: 37, Chinese: "学生工作职位", English: "job" },
  { id: 38, Chinese: "邮箱", English: "email" },
  { id: 39, Chinese: "住址", English: "address" },
  { id: 40, Chinese: " 班主任", English: "headmaster" },
];
export default {
  props: {},
  components: {},
  data() {
    return {
      addDialogVisible: false,
      checkAll: false,
      checkedfields: [],
      fields: fieldOptions,
      isIndeterminate: true,
      filename: "",
      option: [],
      Chinese: [],
    };
  },
  methods: {
    down(data) {
      let blob = new Blob([data], { type: data.type }); //就是这里一点差距
      //兼容ie
      if (window.navigator && window.navigator.msSaveBlob) {
        window.navigator.msSaveBlob(blob, this.filename);
      } else {
        var downloadElement = document.createElement("a"); //模拟一个a标签与asp.net试图操作类似
        var href = window.URL.createObjectURL(blob); //转成链接让其能供人下载
        downloadElement.href = href; //a标签的href
        downloadElement.download = this.filename; //a标签的下载名字
        document.body.appendChild(downloadElement); //注册这个控件将这个组件加到body尾部
        downloadElement.click(); //注销掉
        window.URL.revokeObjectURL(href); //清除生成的链接，会占用一些东西，不知道啥，反正运行慢点
      }
    },
    addDialogClosed() {
      this.addDialogVisible = false;
      this.checkAll = false;
      this.clear();
    },
    clear() {
      this.checkedfields = [];
      this.option = [];
      this.Chinese = [];
    },
    handleCheckAllChange(val) {
      this.checkedfields = val ? fieldOptions : [];
      this.isIndeterminate = false;
    },
    handlecheckedfieldsChange(value) {
      let checkedCount = value.length;
      this.checkAll = checkedCount === this.fields.length;
      this.isIndeterminate =
        checkedCount > 0 && checkedCount < this.fields.length;
    },
    sort() {
      this.checkedfields.sort((a, b) => {
        return b.id > a.id ? -1 : 1;
      });
      this.checkedfields.forEach((item) => {
        this.option.push(item.English);
        this.Chinese.push(item.Chinese);
      });
    },
    async downmessage() {
      this.sort();
      const option = this.option;
      const Chinese = this.Chinese;
      const val = JSON.parse(localStorage.getItem("account"));
      // const res = await this.$http.post("export/person/" + val);
        this.filename = "个人所有信息下载.xlsx";
        const res = await this.$http.post(
          "export/person/" + val,
          { option, Chinese },
          {
            params: this.filter,
            responseType: "blob",
          }
        ); //这里的传递要加responseType:'blob'指定类型，后端不需要处理这个类型，只需要传过去就行
              console.log(res);
        this.down(res.data);
        this.clear();
        this.addDialogVisible=false;
    },
  },
};
</script>

<style>
.a3_adddialog_form {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-around;
}
</style>
<template>
  <div class="a3">
    <!--卡片视图区域-->
    <el-card class="box-card">
      <!--搜索与添加区域
      -->
      <el-row
        :gutter="20"
        style="
          display: flex;
          justify-content: space-between;
          align-items: center;
        "
      >
        <!-- 搜索 clearable:清空数据，@clear:查询数据-->
        <el-col :span="6">
          <el-input
            placeholder="请输入关键词检索"
            v-model="search"
            clearable
            @clear="getUserList"
          >
          </el-input
        ></el-col>
        <el-col :span="3" v-show="copy_show">
          <el-button size="small" @click="show_copydialog = true"
            >批量复制</el-button
          >
        </el-col>
        <el-dialog
          title="复制内容"
          v-show="show_copydialog"
          :visible.sync="show_copydialog"
        >
          <el-input type="textarea" v-model="paster"></el-input>
          <div slot="footer" class="dialog-footer">
            <el-button @click="show_copydialog = false">取 消</el-button>
            <el-button type="primary" @click="pasteMe(paster)">确 定</el-button>
          </div>
        </el-dialog>
        <el-col :span="3" v-show="upload_show">
          <el-button size="small" @click="centerDialogVisible = true"
            >批量导入</el-button
          >
        </el-col>
        <el-dialog
          title="提示"
          :visible.sync="centerDialogVisible"
          width="30%"
          center
        >
          <span>请确定上传的文件符合以下模板</span>
          <br />
          <br />
          <span style="font-weight: bold"
            >注意：非必填的项目为空，数据库将不会对那一项进行修改</span
          >
          <br />
          <br />
          <el-image :src="require('../../assets/demo/demo_6.png')"></el-image>
          <br />
          <el-image :src="require('../../assets/demo/demo.png')"></el-image>
          <span
            slot="footer"
            class="dialog-footer"
            style="display: flex; justify-content: center"
          >
            <el-button type="primary" @click="centerDialogVisible = false"
              >取消</el-button
            >
            <el-upload
              class="upload-demo"
              action="http://192.168.43.143:8001/"
              :before-upload="beforeupload"
              :on-success="handlesuccess"
              :http-request="modeUpload"
              :on-error="handleError"
              :show-file-list="false"
            >
              <el-button type="primary" style="margin-left: 50px"
                >确定</el-button
              >
            </el-upload>
          </span>
        </el-dialog>
        <!-- 批量导出用户信息 -->
        <a3_downdialog></a3_downdialog>
        <el-col :span="3">
          <el-button @click="editAll" size="small">批量编辑</el-button>
        </el-col>
        <el-col :span="3">
          <el-button @click="save" type="primary" size="small"
            >保存批量修改</el-button
          >
        </el-col>
        <el-col :span="3">
          <el-button @click="submit" type="primary" size="small"
            >提交数据</el-button
          >
        </el-col>
      </el-row>
      <!-- 用户列表区域 -->
      <!-- border->带边框,stripe->使用带斑马纹的表格,type="index"->索引列-->
      <el-table
        ref="multipleTable"
        :data="tables"
        border
        stripe
        height="455"
        style="margin-top: 10px"
        @selection-change="handleSelectionChange"
        ><el-table-column type="selection"></el-table-column>
        <!-- <el-table-column type="index" fixed align="center"></el-table-column> -->
        <el-tableColumn label="学号" fixed align="center" prop="account">
          <template slot-scope="scope">
            <span>{{ scope.row.account }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="姓名" prop="name" fixed align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.name"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.name }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="学院" prop="college_title" fixed align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.college_title"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.college_title }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="支部" prop="branch_title" fixed align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.branch_title"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.branch_title }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="首次申请入党时间"
          prop="First_application"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.First_application"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.First_application }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="首次申请入党学期" prop="semester" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.semester"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.semester }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="党组织谈话时间"
          prop="talking_date"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.talking_date"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.talking_date }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="谈话人" prop="talker" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.talker"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.talker }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="入党申请书" prop="apply_letter" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.apply_letter"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.apply_letter }}</span>
          </template>
        </el-tableColumn>

        <el-tableColumn
          label="入党积极分子培训情况"
          prop="courses_for_activists"
          align="center"
          ><template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.courses_for_activists"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.courses_for_activists }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="入党积极分子培训情况备注"
          prop="activists_remarks"
          align="center"
          ><template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.activists_remarks"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.activists_remarks }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="入党积极培训班成绩"
          prop="activists_grade"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.activists_grade"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.activists_grade }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="入党积极分子评优情况"
          prop="activists_appraising"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.activists_appraising"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.activists_appraising }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="入党积极分子结业时间"
          prop="activists_graduation"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.activists_graduation"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.activists_graduation }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="列为入党积极分子时间"
          prop="activists_date"
          align="center"
          ><template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.activists_date"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.activists_date }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="培养联系人1" prop="contacts1" align="center"
          ><template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.contacts1"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.contacts1 }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="培养联系人2" prop="contacts2" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.contacts2"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.contacts2 }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="上传积极分子考察登记表"
          prop="investigation_registration"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.investigation_registration"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.investigation_registration }}</span>
          </template>
        </el-tableColumn>

        <el-tableColumn
          label="发展对象培训班情况"
          prop="courses_for_developer"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.courses_for_developer"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.courses_for_developer }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="发展对象培训情况备注"
          prop="developer_remarks"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.developer_remarks"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.developer_remarks }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="发展对象培训班成绩"
          prop="developer_grade"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.developer_grade"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.developer_grade }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="发展对象培训班评优情况"
          prop="developer_appraising"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.developer_appraising"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.developer_appraising }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="发展对象结业时间"
          prop="developer_graduation"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.developer_graduation"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.developer_graduation }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="列为发展对象时间"
          prop="developer_date"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.developer_date"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.developer_date }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="入党介绍人1" prop="introducer1" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.introducer1"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.introducer1 }}</span>
          </template>
        </el-tableColumn>

        <el-tableColumn label="入党介绍人2" prop="introducer2" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.introducer2"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.introducer2 }}</span>
          </template>
        </el-tableColumn>

        <el-tableColumn label="入党志愿书编号" prop="number" align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.number"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.number }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="群众座谈人员名单"
          prop="mass_discussion"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.mass_discussion"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.mass_discussion }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="发展对象支部大会时间"
          prop="probation_meeting"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.probation_meeting"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.probation_meeting }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="入党志愿书"
          prop="voluntary_letter"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.voluntary_letter"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.voluntary_letter }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn
          label="加入党组织日期"
          prop="probation_date"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.probation_date"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.probation_date }}</span>
          </template></el-tableColumn
        >
        <el-tableColumn
          label="转为正式党员日期"
          prop="formal_date"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.formal_date"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.formal_date }}</span>
          </template></el-tableColumn
        >
        <el-tableColumn
          label="正式党员支部大会时间"
          prop="formal_date"
          align="center"
        >
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.formal_date"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.formal_date }}</span>
          </template></el-tableColumn
        >
        <el-tableColumn label="操作" width="80px" fixed="right" align="center">
          <!-- eslint-disable-next-line -->
          <template slot-scope="scope">
            <!-- 修改用户按钮 -->
            <!-- <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
              @click="showchild(scope.row.account)"
            ></el-button> -->

            <el-button @click="edit(scope.row, scope.$index)" size="mini">{{
              scope.row.show ? "保存" : "修改"
            }}</el-button>

            <!-- 删除用户按钮 -->
            <el-button
              type="danger"
              size="mini"
              style="margin-left: -1px"
              @click="removeUserById(scope.row.account)"
              >删除</el-button
            ></template
          ></el-tableColumn
        >
      </el-table>
    </el-card>
  </div>
</template>

<script>
import Vue from "vue";
import a3_adddialog_form from "@/components/a3_comp/a3_adddialog_form.vue";
import a3_downdialog from "../a3_comp/a3_downdialog.vue";
const temp = [
  {
    account: "",
    name: "",
    college_title: "",
    branch_title: "",
    First_application: "",
    semester: "",
    talking_date: "",
    talker: "",
    apply_letter: "",
    courses_for_activists: "",
    activists_remarks: "",
    activists_grade: "",
    activists_appraising: "",
    activists_appraising: "",
    activists_date: "",
    contacts1: "",
    contacts2: "",
    investigation_registration: "",
    courses_for_developer: "",
    developer_remarks: "",
    developer_grade: "",
    developer_appraising: "",
    developer_graduation: "",
    developer_date: "",
    introducer1: "",
    introducer2: "",
    number: "",
    mass_discussion: "",
    probation_meeting: "",
    voluntary_letter: "",
    probation_date: "",
    formal_date: "",
    formal_date: "",
  },
];
export default {
  components: {
    a3_adddialog_form,
    a3_downdialog,
  },
  data() {
    return {
      // 获取用户列表参数
      search: "",
      userList: [],
      multipleSelection: [],
      filedata: {},
      fileList: [],
      branch_id: "",
      upload_show: true,
      centerDialogVisible: false,
      show_copydialog: false,
      copy_show: false,
      paster: "",
    };
  },
  mounted() {
    this.getUserList();
  },
  computed: {
    tables() {
      let search = this.search.toLowerCase();
      if (search) {
        // tableData是要放在表格中展示的数据
        return this.userList.filter((data) => {
          // 获取对象数组的所有枚举属性，通过some来判断对象中的某一属性是否匹配上，如果匹配上了那么这个对象后面的属性就不用判断了，从而返回整个对象(毕竟我们要看整个对象的值)。
          return Object.keys(data).some((key) => {
            if (data[key] !== null)
              // 对象的属性不为空才进行模糊匹配，否则会报错
              return data[key].toString().toLowerCase().indexOf(search) > -1;
          });
        });
      } else {
        return this.userList; // 如果搜索框没有值，就正常展示表格的所有数据
      }
    },
  },
  methods: {
    pasteMe(e) {
      // 首先对源头进行解析
      let rows = e.split("\n"); // 拆成很多行
      // console.log(rows);
      for (let i = 0; i < rows.length; i++) {
        // console.log(rows[i])
        if (rows[i] != "") {
          // 如果某一行不是空，再按列拆分
          let columns = rows[i].split("\t"); // 已经按列划分
          // console.log("columns" + columns);
          let dataone = {}; // 声明一行数组
          // 读取tableData里的第j对应的key值
          let keys = Object.keys(temp[0]);
          for (let j = 0; j < columns.length; j++) {
            // console.log(this.userList[j]);
            dataone[keys[j]] = columns[j];
          }
          dataone["status"] = 5;
          // console.log(dataone);
          this.userList.push(dataone);
          // console.log(this.userList);
        }
      }
      this.show_copydialog = false;
      this.paster = "";
    },
    modeUpload: function (item) {
      // console.log(item.file);
      this.mode = item.file;
      this.uploadfile();
    },
    handleError(err, file, fileList) {
      // console.log(err,file,fileList)
    },

    handlesuccess(response, file, fileList) {},
    beforeupload(file) {
      if (
        file.type !=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
      ) {
        this.$message({
          message: "请重新点击选择文件传入符合标准的文件",
          type: "warning",
        });
        return false;
      } else return true;
    },
    edit(row, index) {
      row.show = row.show ? false : true;
      Vue.set(this.userList, index, row);
      // 修改后保存
    },
    editAll() {
      this.multipleSelection.map((i, index) => {
        i.show = true;
        Vue.set(this.userList, index, i);
      });
    },
    save() {
      this.multipleSelection.map((i, index) => {
        i.show = false;
        Vue.set(this.userList, index, i);
      });
      this.multipleSelection = [];
      this.toggleSelection();
    },
    submit() {
      this.$confirm(
        "此操作将提交修改信息给数据库, 如还将修改，请继续修改",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        }
      )
        .then(async () => {
          this.userList.map((item) => {
            if (item.activists_appraising == "无") {
              item.activists_appraising = 1;
            } else if (item.activists_appraising == "优") {
              item.activists_appraising = 2;
            }
            if (item.developer_appraising == "无") {
              item.developer_appraising = 1;
            } else if (item.developer_appraising == "优") {
              item.developer_appraising = 2;
            }
          });
          const res = await this.$http.put("user/manyput/", this.userList);
          if (res.status == 200) {
            this.$message({
              type: "success",
              message: res.data.entail,
            });
          } else {
            this.$message({
              type: "erroe",
              message: res.data.entail,
            });
          }
        })
        .catch(async () => {
          this.$message({
            type: "info",
            message: "已取消提交",
          });
        });
    },
    //选
    handleSelectionChange(val) {
      // console.log(val);
      this.multipleSelection = val;
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },

    // 获取用户列表数据
    async getUserList() {
      const val = JSON.parse(localStorage.getItem("id"));
      if (val == 2) {
        this.branch_id = JSON.parse(localStorage.getItem("from_branch"));
        this.temp = await this.$http.get("user/branch/5/" + this.branch_id);
        this.copy_show = true;
      } else if (val == 3) {
        this.upload_show = false;
        const val2 = JSON.parse(localStorage.getItem("from_college"));
        this.temp = await this.$http.get("user/college/5/" + val2);
      } else if (val == 4) {
        this.upload_show = false;
        this.temp = await this.$http.get("user/list/5");
      }
      this.temp.data.map((item) => {
        if (item.activists_appraising == 1) {
          item.activists_appraising = "无";
        } else if (item.activists_appraising == 2) {
          item.activists_appraising = "优";
        }
        if (item.developer_appraising == 1) {
          item.developer_appraising = "无";
        } else if (item.developer_appraising == 2) {
          item.developer_appraising = "优";
        }
        item.show = false;
        return item;
      });
      if (this.temp.status !== 200) return this.$message.error("数据获取失败");
      this.userList = this.temp.data;
    },
    uploadfile() {
      let fd = new FormData();
      fd.append("file_obj", this.mode);
      this.$http.post("impo/formal/" + this.branch_id, fd).then((response) => {
        if (response.status == 200 && response.data.flag == true) {
          this.$message({
            type: "success",
            message: "提交成功!",
          });
          this.getUserList();
        } else {
          if (response.status != 200) {
            this.$message({
              type: "error",
              message: response.data.entail,
            });
          } else {
            this.$message({
              type: "error",
              message: response.data.error,
            });
          }
        }
        this.centerDialogVisible = false;
      });
    },
    // 根据Id删除用户
    async removeUserById(account) {
      const confirmRes = await this.$confirm(
        "此操作将永久删除该用户, 是否继续?",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        }
      ).catch((err) => err);
      // 如果用户确认删除，返回confirm
      // 如果用户取消删除，返回cancel
      if (confirmRes !== "confirm") {
        return this.$message.info("已取消删除");
      }
      const res = await this.$http.delete("user/delete/" + account);
      if (res.status !== 204) {
        return this.$message.error("删除用户失败！");
      }
      this.$message.success("删除用户成功！");
      this.getUserList();
    },
  },
};
</script>

<style>
.userlist_btn {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>


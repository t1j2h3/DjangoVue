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
            placeholder="请输入关键词"
            v-model="search"
            clearable
            @clear="getUserList"
          >
          </el-input
        ></el-col>
        <!-- 添加用户 -->
        <a3_adddialog_form @fatherMethod="getUserList"></a3_adddialog_form>
        <el-col :span="3" v-show="upload_show">
          <el-button size="small" @click="centerDialogVisible = true"
            >批量导入</el-button
          >
        </el-col>
        <el-dialog
          title="上传文件"
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
          <span style="font-weight: bold">批量注册模板</span>
          <br />
          <br />
          <el-image :src="require('../../assets/demo/demo_0.png')"></el-image>
          <br />
          <span style="font-weight: bold">入党申请人模板</span>
          <el-image :src="require('../../assets/demo/demo_1.png')"></el-image>
          <br />
          <br />
          <el-image :src="require('../../assets/demo/demo.png')"></el-image>
          <br />
          <br />
          <span>请选择你要上传的文件类型</span>
          <span slot="footer" class="dialog-footer">
            <el-upload
              class="upload-demo"
              action="http://192.168.43.143:8001/"
              :before-upload="beforeupload"
              :on-success="handlesuccess"
              :http-request="modeUpload"
              :on-error="handleError"
              :show-file-list="false"
            >
              <el-button type="primary" @click="temp = 0">批量注册</el-button>
              <el-button type="primary" @click="temp = 1">入党申请人</el-button>
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
        <el-tableColumn label="操作" width="80px" fixed="right" align="center">
          <!-- eslint-disable-next-line -->
          <template slot-scope="scope">
            <!-- 修改用户按钮 -->

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
    };
  },
  created() {
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
    async modeUpload(item) {
      let res;
      this.mode = item.file;
      if (this.temp == 0) {
        let fd = new FormData();
        fd.append("file_obj", this.mode);
        res = await this.$http.post("impo/register/" + this.branch_id, fd);
        console.log(res)
      } else {
        let fd = new FormData();
        fd.append("file_obj", this.mode);
        res = await this.$http.post("impo/application/" + this.branch_id, fd);
      }
      if (res.status == 200 && res.data.flag == true) {
        this.$message({
          type: "success",
          message: "提交成功!",
        });
        this.getUserList();
      } else {
        if (res.status != 200) {
          this.$message({
            type: "error",
            message: res.data.entail,
          });
        } else {
          this.$message({
            type: "error",
            message: res.data.error,
          });
        }
      }
      this.centerDialogVisible = false;
    },
    handleError(err, file, fileList) {
      // console.log(err,file,fileList)
    },

    handlesuccess(response, file, fileList) {
      // console.log(response, file, fileList);
    },
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
              type: "error",
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
        this.temp = await this.$http.get("user/branch/1/" + this.branch_id);
      } else if (val == 3) {
        this.upload_show = false;
        const val2 = JSON.parse(localStorage.getItem("from_college"));
        this.temp = await this.$http.get("user/college/1/" + val2);
      } else if (val == 4) {
        this.upload_show = false;
        this.temp = await this.$http.get("user/list/1");
        // console.log(this.temp)
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
      // console.log(this.userList);
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


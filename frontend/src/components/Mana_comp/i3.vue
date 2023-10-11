<template>
  <div class="i3">
    <!--卡片视图区域-->
    <el-card class="box-card">
      <!--搜索与添加区域
      -->
      <el-row :gutter="20" style="display: flex; align-items: center">
        <!-- 搜索 clearable:清空数据，@clear:查询数据-->
        <el-col :span="6">
          <el-input
            placeholder="请输入关键词检索"
            v-model="search"
            clearable
            @clear="getOrganList"
          >
          </el-input
        ></el-col>
        <!-- 添加组织 -->
        <i3_adddialog_form
          :data_f="data_all"
          @fatherMethod="getOrganList"
          v-if="getdata"
        ></i3_adddialog_form>
        <!-- 批量导出用户信息 -->
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
      >
        <!-- <el-table-column type="index" fixed align="center"></el-table-column> -->
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
        <el-tableColumn label="班级" prop="branch_title" fixed align="center">
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
        <el-tableColumn label="备注" prop="remarks" fixed align="center">
          <template slot-scope="scope">
            <span v-if="scope.row.show">
              <el-input
                size="mini"
                placeholder="请输入内容"
                v-model="scope.row.remarks"
              ></el-input>
            </span>
            <span v-else>{{ scope.row.remarks }}</span>
          </template>
        </el-tableColumn>
        <el-tableColumn label="操作" fixed="right" align="center">
          <template slot-scope="scope">
            <el-button
              @click="
                scope.row.show
                  ? save(scope.row, scope.row.id)
                  : edit(scope.row, scope.$index)
              "
              size="mini"
              >{{ scope.row.show ? "保存" : "修改" }}</el-button
            >

            <!-- 删除用户按钮 -->
            <el-button
              type="danger"
              size="mini"
              style="margin-left: -1px"
              @click="removeUserById(scope.row.id)"
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
import i3_adddialog_form from "@/components/Mana_comp/i3_adddialog_form.vue";
export default {
  components: {
    i3_adddialog_form,
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
      getdata: false,
      data_all: {
        valplus: "",
        college_title: "",
        college: "",
      },
    };
  },
  // created() {
  //   this.getOrganList();
  // },
  mounted() {
    this.getOrganList();
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
    edit(row, index) {
      row.show = row.show ? false : true;
      Vue.set(this.userList, index, row);
      // 修改后保存
    },

    //选
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },

    // 获取用户列表数据
    async getOrganList() {
      this.data_all.valplus = JSON.parse(localStorage.getItem("id"));
      if (this.data_all.valplus == 3) {
        const val2 = JSON.parse(localStorage.getItem("from_college"));
        this.temp = await this.$http.get("branch/find/" + val2);
        this.data_all.college_title = this.temp.data[0].college_title;
        this.data_all.college = this.temp.data[0].college;
        this.getdata = true;
      } else if (this.data_all.valplus == 4) {
        this.temp = await this.$http.get("college/all/");
        this.getdata = true;
      }
      this.temp.data.map((item) => {
        item.show = false;
        return item;
      });
      if (this.temp.status !== 200) return this.$message.error("数据获取失败");
      this.userList = this.temp.data;
    },
    async save(row, id) {
      if (this.data_all.valplus == 3) {
        const res = await this.$http.put("branch/all/" + id, row);
        if (res.status !== 200) {
          return this.$message.error("保存失败！");
        } else {
          this.$message.success("保存成功！");
          row.show = false;
          this.getOrganList();
        }
      } else if (this.data_all.valplus == 4) {
        const res = await this.$http.put("college/all/" + id, row);
        if (res.status !== 200) {
          return this.$message.error("保存失败！");
        } else {
          this.$message.success("保存成功！");
          row.show = false;
          this.getOrganList();
        }
      }
    },
    // 根据Id删除用户
    async removeUserById(id) {
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
      if (this.data_all.valplus == 3) {
        const res = await this.$http.delete("branch/all/" + id);
        if (res.status !== 204) {
          return this.$message.error("删除用户失败！");
        }
        this.$message.success("删除用户成功！");
        this.getOrganList();
      } else if (this.data_all.valplus == 4) {
        const res = await this.$http.delete("college/all/" + id);
        if (res.status !== 204) {
          return this.$message.error("删除用户失败！");
        }
        this.$message.success("删除用户成功！");
        this.getOrganList();
      }
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


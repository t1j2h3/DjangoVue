<template>
  <div class="f3">
    <el-table :data="tables" style="width: 100%" border height="540" stripe>
      <el-table-column label="学号" prop="account"> </el-table-column>
      <el-table-column label="姓名" prop="name"> </el-table-column>
      <el-table-column label="学院" prop="college_title"> </el-table-column>
      <el-table-column label="班级" prop="branch_title"> </el-table-column>
      <el-table-column label="申请信息" prop="message"></el-table-column>
      <el-table-column align="right">
        <template slot="header" slot-scope="scope">
          <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
        </template>
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)"
            v-show="scope.row.state == '1'"
            >同意</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            v-show="scope.row.state == '1'"
            >拒绝</el-button
          >
          <div class="text" v-show="scope.row.state == '2'">已同意</div>
          <div class="text" v-show="scope.row.state == '3'">已拒绝</div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      message1: "申请注册",
      tableData: [],
      search: "",
    };
  },
  computed: {
    tables() {
      let search = this.search.toLowerCase();
      if (search) {
        // tableData是要放在表格中展示的数据
        return this.tableData.filter((data) => {
          // 获取对象数组的所有枚举属性，通过some来判断对象中的某一属性是否匹配上，如果匹配上了那么这个对象后面的属性就不用判断了，从而返回整个对象(毕竟我们要看整个对象的值)。
          return Object.keys(data).some((key) => {
            if (data[key] !== null)
              // 对象的属性不为空才进行模糊匹配，否则会报错
              return data[key].toString().toLowerCase().indexOf(search) > -1;
          });
        });
      } else {
        return this.tableData; // 如果搜索框没有值，就正常展示表格的所有数据
      }
    },
  },
  created() {
    this.showregmessage();
  },
  mounted() {
    document.getElementsByTagName("html")[0].style.overflowX = "visible";
  },
  methods: {
    async showregmessage() {
      const val = JSON.parse(localStorage.getItem("id"));
      if (val == 2) {
        const val1 = JSON.parse(localStorage.getItem("from_branch"));
        const res = await this.$http.get("registration/branch/" + val1);
        res.data.map((item) => {
          item.message = "申请注册";
          return item;
        });
        const res2 = await this.$http.get(
          // "transferorganization/branch/" + val1
        );
        console.log(res2);
        const res3 = res2.data.map((item) => {
          return {
            college_title: item.past_college_t,
            branch_title: item.past_branch_t,
            name: item.name,
            account: item.account,
            state: item.state,
            message: "申请关系转接",
            date: item.date,
            id: item.id,
            new_branch: item.new_branch,
            new_college: item.new_college,
          };
        });
        this.tableData = res.data.concat(res3);
      } else if (val == 3) {
        const val2 = JSON.parse(localStorage.getItem("from_college"));
        const res = await this.$http.get("registration/college/" + val2);
        res.data.map((item) => {
          item.message = "申请注册";
          return item;
        });
        const res2 = await this.$http.get(
          // "transferorganization/college/" + val2
        );
        console.log(res2);
        const res3 = res2.data.map((item) => {
          return {
            college_title: item.past_college_t,
            branch_title: item.past_branch_t,
            name: item.name,
            account: item.account,
            state: item.state,
            message: "申请关系转接",
            date: item.date,
            id: item.id,
            new_branch: item.new_branch,
            new_college: item.new_college,
          };
        });
        this.tableData = res.data.concat(res3);
      } else if (val == 4) {
        const res = await this.$http.get("registration/all/");
        console.log(res);
        res.data.map((item) => {
          item.message = "申请注册";
          return item;
        });
        this.tableData = res.data;
      }
    },
    async handleEdit(index, row) {
      let temp = 2;
      let temp2 = row.id;
      row.state = temp;
      if (row.message == "申请注册") {
        const res = await this.$http.put("registration/update/" + temp2, row);
      } else {
        console.log(row);

        const res2 = await this.$http.put(
          "transferorganization/update/" + temp2,
          row
        );
        console.log(res2);
      }
    },
    async handleDelete(index, row) {
      let temp = 3;
      let temp3 = row.id;
      row.state = temp;
      if (row.message == "申请注册") {
        const res = await this.$http.put("registration/update/" + temp3, row);
      } else {
        const res2 = await this.$http.put(
          "transferorganization/update/" + temp3,
          row
        );
      }
    },
  },
};
</script>

<style>
.f3 {
  width: 100%;
  height: 100%;
}
.text {
  display: flex;
  justify-content: center;
}
</style>

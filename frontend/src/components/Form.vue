<template>
<div id="app">
  <!-- {{ msg }} -->

  <!-- Form submit new issue -->
  <form @submit.prevent="submitForm">  <!-- "createIssue" -->

    <div class="form-ui">
      <label for="id">Enter your User ID Number: </label>
      <input type="text" v-model="issue.uid" placeholder="UID" name="id" id="id" required />
    </div>
    <div class="form-ui">
      <label for="problem">Enter problem description: </label>
      <input type="text" v-model="issue.description" placeholder="Description" name="problem" id="problem" maxlength="300" required />
    </div>
    <div class="form-ui">
      <label for="serial">Enter device serial number: </label>
      <input type="text" v-model="issue.serial" placeholder="Serial" name="serial" id="serial" maxlength="64" required />
    </div>

    <div class="form-ui">
      <label for="indicator1">Choose indicator1 status:</label>
      <select v-model="issue.indicator1" placeholder="indicator1" id="indicator1" name="indicator1" required>
        <option value="on">On</option>
        <option value="off">Off</option>
        <option value="blinking">Blinking</option>
      </select>
    </div>

    <div class="form-ui">
      <label for="indicator2">Choose indicator2 status:</label>
      <select v-model="issue.indicator2" placeholder="indicator2" id="indicator2" name="indicator2" required>
        <option value="on">On</option>
        <option value="off">Off</option>
        <option value="blinking">Blinking</option>
      </select>
    </div>

    <div class="form-ui">
      <label for="indicator3">Choose indicator3 status:</label>
      <select v-model="issue.indicator3" placeholder="indicator3" id="indicator3" name="indicator3" required>
        <option value="on">On</option>
        <option value="off">Off</option>
        <option value="blinking">Blinking</option>
      </select>
    </div>

    <div class="form-ui" id="submit">
      <input type="submit" value="Submit" />
    </div>

  </form>

  <!-- SHOW DATA ON TABLE -->
  <table class="table">
    <thead>
      <th>User ID</th>
      <th>Description</th>
      <th>Serial</th>
      <th>indicator1</th>
      <th>indicator2</th>
      <th>indicator3</th>
      <th>Response</th>
    </thead>
    <tbody>
      <tr v-for="issue in issues" :key="issue.id" @dblclick="$data.issue = issue">
        <td>{{ issue.uid }}</td>
        <td>{{ issue.description }}</td>
        <td>{{ issue.serial }}</td>
        <td>{{ issue.indicator1 }}</td>
        <td>{{ issue.indicator2 }}</td>
        <td>{{ issue.indicator3 }}</td>
        <td>{{ issue.response }}</td>
        <td>
          <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteIssue(issue)">x</button>
        </td>
      </tr>
    </tbody>
  </table>

</div>
 
</template>

<script>
 

export default {
  name: 'Form',
  data(){
    return {
      // msg: 'Hello All'
      issue: {},         
      issues: []
    }
  },
  async created(){
    //var response = await fetch('http://127.0.0.1:8000/api/issues/')
    //this.issues = await response.json();
    await this.getIssues();
  },

  methods: {
    submitForm(){
      if (this.issue.id === undefined){
        this.createIssue();
      } else {
        this.editIssue();
      }
    },

    async getIssues(){
      var response = await fetch('http://127.0.0.1:8000/api/issues/') 
      this.issues = await response.json();
    },

    async createIssue(){
      await this.getIssues();
      /*var response = */
      await fetch('http://127.0.0.1:8000/api/issues/', {
        method: 'post',
        headers:  {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.issue)
      });
      //this.issues.push(await response.json());
      await this.getIssues();
      this.issue = {};
    },

    async editIssue(){
      await this.getIssues();
      await fetch(`http://127.0.0.1:8000/api/issues/${this.issue.id}/`, {
        method: 'put', 
        headers:  {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.issue)
      });
      await this.getIssues();
      this.issue = {};
    },

    async deleteIssue(issue){
      await this.getIssues();
      await fetch(`http://127.0.0.1:8000/api/issues/${issue.id}/`, {
        method: 'delete', 
        headers:  {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.issue)
      });
      await this.getIssues();
    },

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

p {
  font-size: 18px;
}

form.form-ui {
  display: table;
  margin: 15px;
}

div.form-ui {
  display: table-row;
}

input {
  display: table-cell;
  margin-bottom: 10px;
}

label {
  padding-right: 10px;
}
</style>

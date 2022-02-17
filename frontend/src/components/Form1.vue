<template>
  <form @submit.prevent="createForm" class="form-ui">
     <div class="form-ui">
      <label for="id">Enter your user ID Number: </label>
      <input type="text" v-model="id" placeholder="ID" name="id" id="id" required />
    </div>
    <div class="form-ui">
      <label for="problem">Enter problem desciption: </label>
      <input type="text" v-model="problem" placeholder="Description" name="problem" id="problem" maxlength="300" required />
    </div>
    <div class="form-ui">
      <label for="serial">Enter device serial number: </label>
      <input type="text" v-model="serial" placeholder="Serial" name="serial" id="serial" maxlength="64" required />
    </div>

    <div class="form-ui">
      <label for="indicator1">Choose indicator1 status:</label>
      <select v-model="indicator1" placeholder="indicator1" id="indicator1" name="indicator1" required>
        <option value="on">On</option>
        <option value="off">Off</option>
        <option value="blinking">Blinking</option>
      </select>
    </div>

    <div class="form-ui">
      <label for="indicator2">Choose indicator2 status:</label>
      <select v-model="indicator2" placeholder="indicator2" id="indicator2" name="indicator2" required>
        <option value="on">On</option>
        <option value="off">Off</option>
        <option value="blinking">Blinking</option>
      </select>
    </div>

    <div class="form-ui">
      <label for="indicator3">Choose indicator3 status:</label>
      <select v-model="indicator3" placeholder="indicator3" id="indicator3" name="indicator3" required>
        <option value="on">On</option>
        <option value="off">Off</option>
        <option value="blinking">Blinking</option>
      </select>
    </div>

    <div class="submit" id="submit">
      <input type="submit" value="Submit" />
    </div>

  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "Form",
  data() {
    return {
      id: '',
      problem: '',
      serial: '',
      indicator1: '',
      indicator2: '',
      indicator3: ''
    };
  },
  methods: {
    createForm() {
    // POST request using axios with error handling
    const formData = { 
          id: this.id,
          problem: this.problem,
          serial: this.serial,
          indicator1: this.indicator1,
          indicator2: this.indicator2,
          indicator3: this.indicator3
           };
    axios.post("http://127.0.0.1:8000/api/issues/", formData) 
      .then(response => console.log(response))
      //.then(response => this.formDataId = response.data.id)
      .catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error);
      });
    }
  }
};
</script>

<style scoped>
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

label,
input {
  display: table-cell;
  margin-bottom: 10px;
}

label {
  padding-right: 10px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}

</style>
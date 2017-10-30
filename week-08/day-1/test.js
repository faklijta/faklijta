var student = {
    name: "John Doe",
    greet: function() {
      console.log(this.name);
    }
  };
  
  student.greet(); // prints greet

  var volvo = {
    type: "Volvo",
    fuel: 23,
    consumption: 0.06,
    kms: 43000,
    ride: function (km) {
      this.kms += km;
      this.fuel -= km * this.consumption; 
      return this.kms;
    } 
  };
  console.log(volvo.ride(43))
  
  var ferrari = {
    type: "Ferrari",
    fuel: 0,
    consumption: 0.12,
    kms: 9000,
    ride: function (km) {
      this.kms += km;
      this.fuel -= km * this.consumption; 
    }
  };
  
  function refuel(liters) {
    this.fuel += liters;
    return "fueled"
  }
  
  let ferrariRefuel = refuel.bind(ferrari);
  console.log(ferrariRefuel(52))
  console.log(ferrari)
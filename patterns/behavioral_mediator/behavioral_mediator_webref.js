//  OfficialDealer like mediator
class OfficialDealer {
    constructor() {
      this.customers = [];
    }
    
    orderAuto(customer, auto, info) {
      const name = customer.getName();
      console.log(`Order name: ${name}. Order auto is ${auto}`);
      console.log(`Additional info: ${info}`);
      this.addToCustomersList(name);
    }
    
    addToCustomersList(name) {
      this.customers.push(name);
    }
    
    getCustomerList() {
      return this.customers;
    }
  };
  
  class Customer {
    constructor(name, dealerMediator) {
      this.name = name;
      this.dealerMediator = dealerMediator;
    }
       
    getName() {
      return this.name;
    }
       
    makeOrder(auto, info) {
      this.dealerMediator.orderAuto(this, auto, info)
    }
  };


  // ---
  const mediator = new OfficialDealer();
  const cust1 = new Customer('name1', mediator);
  const cust2 = new Customer('name2', mediator);

  cust1.makeOrder('tesla', '+ autopilot');
  cust2.makeOrder('bmw', '+ parktronik');

  console.log(mediator.getCustomerList());
  
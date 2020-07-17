function sumList(arr) {
  let sum = arr.reduce((a,b) => {
    return a + b
  }, 0);
  return sum
}

function sumExpenses() {
  let prop_tax_arr = document.querySelectorAll('#prop_tax_monthly');
  let prop_tax = [];

  prop_tax_arr.forEach((item, i) => {
    let string = item.innerHTML.split("$");
    let number = Number(string[1]);
    console.log(string);
    console.log(Number(number));
    prop_tax.push(number);
  });

  let insurance_arr = document.querySelectorAll('#insurance_monthly');
  let insurance = [];

  insurance_arr.forEach((item, i) => {
    let string = item.innerHTML.split("$");
    let number = Number(string[1]);
    insurance.push(number);

  });

  let expense_arr = document.querySelectorAll('#expenses_monthly');
  let expense = [];

  expense_arr.forEach((item, i) => {
    let string = item.innerHTML.split("$");
    let number = Number(string[1]);
    expense.push(number);

  });

  console.log(prop_tax);
  console.log(insurance);
  console.log(expense);
  let prop_tax_sum = sumList(prop_tax);
  let insurance_sum = sumList(insurance);
  let expenses_sum = sumList(expense);
  let total_sum = prop_tax_sum + insurance_sum + expenses_sum;
  let total_rows = 1 + prop_tax.length + insurance.length + expense.length
  console.log(total_sum);

  let table = document.getElementById('expense-table');
  let row = table.insertRow(total_rows);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);

    // Add some text to the new cells:
    cell1.innerHTML = "Total";
    cell2.innerHTML = `$${total_sum}`;
    cell3.innerHTML = `$${total_sum * 12}`;

    row.className = 'table-active';
  let noi1 = document.getElementById('noi-1');
  let noi2 = document.getElementById('noi-2');
  let rent = Number(document.getElementById('rent').innerHTML);
  let price = Number(document.getElementById('price').innerHTML);
  let cap_rate = document.getElementById('cap-rate')
  console.log(rent);
  noi1.innerHTML = `$${rent - total_sum}`;
  noi2.innerHTML = `$${(rent * 12) - (total_sum * 12)}`

  cap_rate.innerHTML = ((rent * 12) - (total_sum * 12)) / price
}


sumExpenses();

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);


function copyTextToClipboard(text) {
  var textArea = document.createElement("textarea");

  //
  // *** This styling is an extra step which is likely not required. ***
  //
  // Why is it here? To ensure:
  // 1. the element is able to have focus and selection.
  // 2. if element was to flash render it has minimal visual impact.
  // 3. less flakyness with selection and copying which **might** occur if
  //    the textarea element is not visible.
  //
  // The likelihood is the element won't even render, not even a flash,
  // so some of these are just precautions. However in IE the element
  // is visible whilst the popup box asking the user for permission for
  // the web page to copy to the clipboard.
  //

  // Place in top-left corner of screen regardless of scroll position.
  textArea.style.position = 'fixed';
  textArea.style.top = 0;
  textArea.style.left = 0;

  // Ensure it has a small width and height. Setting to 1px / 1em
  // doesn't work as this gives a negative w/h on some browsers.
  textArea.style.width = '2em';
  textArea.style.height = '2em';

  // We don't need padding, reducing the size if it does flash render.
  textArea.style.padding = 0;

  // Clean up any borders.
  textArea.style.border = 'none';
  textArea.style.outline = 'none';
  textArea.style.boxShadow = 'none';

  // Avoid flash of white box if rendered for any reason.
  textArea.style.background = 'transparent';


  textArea.value = text;

  document.body.appendChild(textArea);

  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
  } catch (err) {
    console.log('Oops, unable to copy');
  }

  document.body.removeChild(textArea);
}

function CopyLink() {
  copyTextToClipboard(location.href);
}

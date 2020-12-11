import React, {userState, useEffect } from 'react';

function Transaction(){

    useEffect(() =>{
        fetchTransactions();
    }, [])

    const [transactions, setTransactions] = useState([]);

    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': 'WaiaCA14j19ibdk6JZR3D5E03Y8I21HQ3nDMh3c5'
        },

        body: JSON.stringify({
            'custID': '1'
        })
    }
}

const fetchTransactions = async() => {
    const data = await fetch("https://cors-anywhere.herokuapp.com/http://u8fpqfk2d4.execute-api.ap-southeast-1.amazonws.com/techtrek2020/transaction/add");

    const transactions = await data.json();
    console.log(transactions);
    setTransactions(transactions);
}

return(
    <table>
        <tr>
            <th>Date</th>
            <th>payeeID</th>
            <th>Amount</th>
            <th>Category</th>
            <th>eGift</th>
            <th>message</th>
        </tr>
        { transactions.map(transaction =>(
            <tr>
                <th>{transaction.dateTime}</th>
                <th>{transaction.payeeID}</th>
                <th>${transaction.amount}</th>
                <th>{transaction.expensesCat}</th>
                <th>{transaction.message}</th>
            </tr>
        ))}
    </table>
)
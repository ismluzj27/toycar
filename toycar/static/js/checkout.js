document.addEventListener('DOMContentLoaded', function () {
    const paymentMethod = document.getElementById('paymentMethod');
    const ccFields = document.getElementById('creditCardFields');
    const paypalField = document.getElementById('paypalField');
    const bankField = document.getElementById('bankField');

    paymentMethod.addEventListener('change', () => {
        ccFields.classList.add('d-none');
        paypalField.classList.add('d-none');
        bankField.classList.add('d-none');

        if (paymentMethod.value === 'Credit Card') {
            ccFields.classList.remove('d-none');
        } else if (paymentMethod.value === 'PayPal') {
            paypalField.classList.remove('d-none');
        } else if (paymentMethod.value === 'Bank Transfer') {
            bankField.classList.remove('d-none');
        }
    });

    function isFutureDate(exp) {
        const [mm, yy] = exp.split('/');
        if (!mm || !yy || mm.length !== 2 || yy.length !== 2) return false;
        const expDate = new Date(`20${yy}`, mm);
        const today = new Date();
        return expDate > today;
    }

    window.checkFilledOut = function () {
        const name = document.getElementById('fullName').value.trim();
        const email = document.getElementById('email').value.trim();
        const address = document.getElementById('address').value.trim();
        const method = paymentMethod.value;

        if (!name || !email || !address || !method) {
            alert("Please fill in all required fields.");
            return;
        }

        if (method === 'Credit Card') {
            const card = document.getElementById('cardno').value.trim();
            const exp = document.getElementById('expdate').value.trim();
            const cvv = document.getElementById('cvv').value.trim();

            if (!/^\d{16}$/.test(card)) {
                alert("Card number must be 16 digits.");
                return;
            }

            if (!/^\d{2}\/\d{2}$/.test(exp) || !isFutureDate(exp)) {
                alert("Expiration must be valid and in the future (MM/YY).");
                return;
            }

            if (!/^\d{3}$/.test(cvv)) {
                alert("CVV must be 3 digits.");
                return;
            }
        }

        if (method === 'PayPal') {
            const paypalEmail = document.getElementById('paypalEmail').value.trim();
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(paypalEmail)) {
                alert("Enter a valid PayPal email.");
                return;
            }
        }

        if (method === 'Bank Transfer') {
            const bankAcc = document.getElementById('bankAccount').value.trim();
            if (!/^\d+$/.test(bankAcc)) {
                alert("Bank account number must be numeric.");
                return;
            }
        }

        // Replace this with Django-generated URL in production
        window.location.href = "/ordered/";
    };
});
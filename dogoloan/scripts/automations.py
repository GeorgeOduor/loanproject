from django.db import models, transaction


class TransactionManager(models.Manager):
    @transaction.atomic
    def create_borrowing_transaction(self, borrower,lender,product, principle, interest, excise_duty=0):
        # Create the loan disbursement record
        
        loan_disbursement = self.create(
            borrower         = borrower,
            lender           = lender,
            product          = product,
            transaction_type = 'Loan Disbursement',
            debit            = principle,
            description      = 'Loan Disbursement',
            balance     = principle 
            )
        # Create the interest record
        interest_record = self.create(
            borrower         = borrower,
            lender           = lender,
            product          = product,
            transaction_type = 'Interest Charges',
            debit            = interest,
            description      = f'{round(interest/principle*100)}% Interest charged on loan',
            balance     =  principle + interest,
            )
        if excise_duty > 0:
            # Create the excise duty record
            excise_duty_record = self.create(
                borrower         = borrower,
                lender           = lender,
                product          = product,
                transaction_type = 'Excise Duty',
                debit            = excise_duty,
                description      = 'Excise Duty',
                balance     = principle + interest + excise_duty,
                )

        return loan_disbursement, interest_record, excise_duty_record

    def create_repayment_transaction(self, borrower,lender,product, amount,current_loan_balance,mpesa_trx_id=""):
        if current_loan_balance == 0:
            raise Exception("You have no outstanding loan balance")
        # Create the loan repayment record
        new_loan_balance = float(current_loan_balance) - amount
        if new_loan_balance < 0:
            refund = abs(new_loan_balance)
            amount = amount - refund
            current_loan_balance = 0
        else:
            current_loan_balance = new_loan_balance
            refund = 0
        
        loan_repayment = self.create(
            borrower         = borrower,
            lender           = lender,
            product          = product,
            transaction_type = 'Loan Repayment',
            credit           = amount,
            description      = f'Loan Repayment of {amount} via MPESA - {mpesa_trx_id}',
            balance          = current_loan_balance
            )
        if current_loan_balance == 0:
            message =f"Loan Repayment of {amount} via MPESA - {mpesa_trx_id} was successful.Your loan is fully settled." 
        else:
            message =f"Loan Repayment of {amount} via MPESA - {mpesa_trx_id} was successful. Your new loan balance is Ksh {current_loan_balance}."
        return loan_repayment, message

def get_loan_balance(borrower_id,model):
    try:
        # get loan balance
        loan_balance = model.objects.filter(borrower=borrower_id).order_by('-transaction_date')[0]
        return loan_balance
    except Exception as e:
        print(f"{e}","------------------x")
        return 0


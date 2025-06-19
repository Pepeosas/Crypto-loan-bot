
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "YOUR_BOT_TOKEN"

loan_amounts = {
    "$5,000": 5000,
    "$10,000": 10000,
    "$20,000": 20000,
    "$50,000": 50000,
    "$100,000": 100000
}

repayment_durations = ["30 days", "2 months", "6 months", "1 year"]

BTC_ADDRESS = "bc1qcfqc890wjluc9959wge620kfwepcl0693c34gp"
USDT_ADDRESS = "0x67FBA45b536b54519c080f929B20B17901AAc86a"

def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "🤖 Welcome to CryptoLoan Vault!

"
        "We offer secure BTC and USDT loans from $5,000 to $100,000.

"
        "💰 Network fee: 10% of the loan amount, paid to receive the loan.
"
        f"BTC: `{BTC_ADDRESS}`
"
        f"USDT (BEP20): `{USDT_ADDRESS}`

"
        "🕒 Repayment Options:
- 30 days
- 2 months
- 6 months
- 1 year

"
        "📤 After paying the network fee, click **Confirm Payment** and submit proof.
"
        "✅ We will validate and send your loan.

"
        "🛟 Need help buying crypto or cashing out to your bank? Use the button below.
"
        "🔐 *We never ask for your private keys or recovery phrase.*"
    )
    buttons = [
        [InlineKeyboardButton(amount, callback_data=amount)] for amount in loan_amounts
    ]
    buttons.append([InlineKeyboardButton("💬 Contact Support", url="https://t.me/support_bot_here")])
    update.message.reply_text(welcome_text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode='Markdown')

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    amount_str = query.data
    amount = loan_amounts.get(amount_str, 0)
    fee = amount * 0.10
    message = (
        f"💵 You selected a loan of {amount_str}.

"
        f"📌 A network fee of 10% (${fee:,.2f}) must be paid to receive the loan.

"
        f"Send payment to:
"
        f"BTC Address: `{BTC_ADDRESS}`
"
        f"USDT Address (BEP20): `{USDT_ADDRESS}`

"
        "After sending payment, click **Confirm Payment** and submit proof to @Pepeosas32 for validation."
    )
    query.edit_message_text(message, parse_mode='Markdown')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    print("Bot is running with polling on PythonAnywhere...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

# Dana's answers

| Question | Answer |
|---|---|
| What kinds of deal? | Just "X% off the whole order". That's all the next campaign uses. |
| More than one code per order? | One code per order. |
| Expiry or usage limits? | No expiry for now. We'll ask engineering to remove a code when its campaign ends. |
| Who creates codes? | Engineering adds them, about three a quarter. |
| A code that doesn't exist? | Reject it and tell the customer the code isn't valid. Don't charge them full price without telling them. |
| The box is left empty? | Treat it as no code. The order goes through at full price. |
| How do customers type codes? | Any way. `save10` and ` SAVE10 ` with stray spaces should both work. |
| A fraction of a cent? | Always in the customer's favour. Finance won't accept anything else. |

## If it asks a follow-up

These came up in practice runs after the first answers. Paste the ones it asks about.

| Follow-up | Answer |
|---|---|
| Should the response show the discount or the original total? | Keep the response as it is: just `total_cents`. |
| What should the error say? | `promo code is not valid` |
| What if `promo_code` isn't text (a number, a list)? | Reject it with a 400, the same as an unknown code. |
| Unknown product and unknown code in one order? | The product error wins. Report that one. |

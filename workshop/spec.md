# Spec: Promo codes at checkout

**Goal:** A customer can enter one promo code at checkout and get a percentage off the whole order.

**Acceptance criteria**
1. Given no `promo_code`, or an empty one, when checkout runs, then the order goes through at
   full price.
2. Given `SAVE10` (10%) and a 1250 cent order, when checkout runs, then `total_cents` is 1125.
3. Given a discount with a fraction of a cent, when checkout runs, then the customer gets the
   fraction: `SAVE10` on 9 t-shirts (17991 cents) gives a total of 16191.
4. Given `save10` or ` SAVE10 `, when checkout runs, then it works like `SAVE10`.
5. Given a code that doesn't exist, when checkout runs, then the status is 400, `error` says the
   code isn't valid, and there is no `total_cents`.
6. Given a `promo_code` that isn't a single string, such as a list of codes, when checkout runs,
   then the status is 400 with the same error, not an exception.

**Out of scope** (pruned, and why)
- Fixed amounts, per-product deals, buy-one-get-one: the campaign only uses percentage off.
- Several codes per order: one code per order.
- Expiry and usage limits: engineering removes a code when its campaign ends.
- Admin tools: engineering adds about three codes a quarter, in `shop/repo.py`.
- A discount amount in the response: nobody asked for it.

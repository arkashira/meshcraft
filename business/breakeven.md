 # Breakeven Analysis

## Cost per Active User (CPU)

The cost per active user (CPU) for `meshcraft` is calculated based on the following assumptions:

- Compute: $0.02 per hour per instance (AWS EC2 t3.small)
- Storage: $0.023 per GB per month (AWS S3 Standard)
- Bandwidth: $0.09 per GB (AWS Data Transfer Out)

Assuming an active user generates 1 GB of data per month, uses the service for 8 hours per month, and transfers 5 GB of data per month:

```
CPU = (0.02 * 8) + (0.023 * 1) + (0.09 * 5) = $0.533 per month
```

## Pricing Tiers

To maximize revenue and attract a broad range of users, we will offer three pricing tiers:

1. **Starter**: $10/month
   - 1 instance
   - 10 GB storage
   - 10 GB bandwidth

2. **Pro**: $30/month
   - 3 instances
   - 30 GB storage
   - 30 GB bandwidth
   - Priority support

3. **Enterprise**: Custom pricing
   - Unlimited instances
   - Custom storage and bandwidth
   - Dedicated account manager
   - SLA

## Customer Acquisition Cost (CAC)

The Customer Acquisition Cost (CAC) for `meshcraft` is estimated to be $500 per customer, including marketing, sales, and onboarding costs.

## Lifetime Value (LTV) Estimate

The Lifetime Value (LTV) for `meshcraft` is difficult to estimate accurately without more data on customer behavior and churn rates. However, based on initial assumptions, we can make a rough estimate:

- Average Revenue per User (ARPU): $10 (Starter tier)
- Churn rate: 5% per month
- Average customer lifespan: 24 months

```
LTV = (ARPU * (1 - churn rate)^n) / CAC
LTV = ($10 * (1 - 0.05)^24) / $500 ≈ $240
```

## Break-even Users Count

To break even, we need to find the number of users required to cover the CAC:

```
Break-even users = CAC / CPU
Break-even users = $500 / $0.533 ≈ 938
```

## Path to $10K MRR

To reach a monthly recurring revenue (MRR) of $10,000, we need to find the number of users required for each pricing tier:

1. **Starter**: $10,000 / $10 = 1,000 users
2. **Pro**: $10,000 / $30 = 333 users
3. **Enterprise**: Custom pricing

Assuming a mix of Starter and Pro users, we can estimate the number of each tier needed:

- Starter: 800 users
- Pro: 233 users

This equates to a total of 1,033 users to reach a MRR of $10,000.
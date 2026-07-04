There is an Apache-style access log at `/app/access.log`. Write a JSON summary to
`/app/report.json`.

Success criteria:

1. The report file must be valid JSON.
2. The JSON object must contain exactly these keys: `total_requests`, `unique_ips`,
   and `top_path`.
3. `total_requests` must be the number of non-empty log lines.
4. `unique_ips` must be the number of distinct client IP addresses.
5. `top_path` must be the request path with the highest request count.

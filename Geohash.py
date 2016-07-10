class GeoHash:
    # @param {double} latitude, longitude a location coordinate pair
    # @param {int} precision an integer between 1 to 12
    # @return {string} a base32 string
    def encode(self, latitude, longitude, precision):
        # Write your code here
        def helper(step, val, start, end):
            if step <= 0:
                return ""
            mid = (start + end) / 2.0
            if val <= mid:
                return '0' + helper(step - 1, val, start, mid)
            else:
                return '1' + helper(step - 1, val, mid, end)

        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        lat = helper(30, latitude, -90, 90)
        lng = helper(30, longitude, -180, 180)
        vals = [i + j for i, j in zip(lng, lat)]
        vals = ''.join(vals)
        ans = [0] * precision
        for i in range(0, precision * 5, 5):
            index = int(vals[i:i + 5], 2)
            ans[i / 5] = _base32[index]
        return ''.join(ans)

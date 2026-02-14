-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Example configs: https://github.com/LunarVim/starter.lvim
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny
lvim.transparent_window = true
vim.opt.number = true
lvim.colorscheme = "pywal"
vim.opt.termguicolors = true
vim.opt.shiftwidth = 4 -- Size of an indent
vim.opt.tabstop = 4    -- Number of spaces tabs count for
vim.opt.softtabstop = 4
vim.opt.expandtab = true -- Use spaces instead of tabs

lvim.plugins = {
  {
    "norcalli/nvim-colorizer.lua",
    config = function()
      require("colorizer").setup({
        "*",
      })
    end
  },
  { "AlphaTechnolog/pywal.nvim", name = "pywal" },
}

-- Refresh colors when the window gains focus
vim.api.nvim_create_autocmd("FocusGained", {
    pattern = "*",
    callback = function()
        -- Reload the colorscheme
        vim.cmd("colorscheme " .. lvim.colorscheme)
        -- If you use transparency, re-apply it here
        vim.api.nvim_set_hl(0, "Normal", { bg = "none", ctermbg = "none" })
    end,
})

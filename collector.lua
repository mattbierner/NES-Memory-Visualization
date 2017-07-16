outDir = ".\\output_test\\"
count = 0

function after_frame()
    gui.savescreenshotas(string.format("%s\\%d.png", outDir, count))

    local data = memory.readbyterange(0, 0x0800)

    emu.print(string.format("frame %d", count))

    local out = assert(io.open(string.format("%s\\%d.data", outDir, count), "wb"))
    out:write(data)
    assert(out:close())
    count = count + 1
end

os.execute("mkdir " .. outDir)

emu.speedmode("normal")
emu.registerafter(after_frame)

while true do
    emu.frameadvance()
end 
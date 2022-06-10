ps --no-headers au | grep -sv -E '(ssh|sshd|scp|ps|bash)' >> k200481/ps_list
mkdir k200481/dumps
python3 k200481/scripts/dump_mem.py k200481/ps_list k200481/dumps
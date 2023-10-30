import re
# from ansible import errors


def normalize_shell_cmd_args(cmd):
    # reg_cmd_lines = r".*(\n|;)"
    # [^'\"\s;&] no space, no quote
    arg_chars = "[^'\"\s;&\|]"
    reg_with_double_quote = r"{0}+?=\"[^\"]*?\"".format(arg_chars)
    reg_with_single_quote = r"{0}+?='[^']*?'".format(arg_chars)
    reg_no_quote = r"{0}+".format(arg_chars)
    reg_noquote_for_replace = r"^({0}+?=)({0}*)$".format(arg_chars)
    reg_single_for_replace = r"({0}+?)'(.*?)'".format(arg_chars)
    reg_with_single_quote = r"{0}+?='.*?'".format(arg_chars)
    reg_with_double_quote = r"{0}+?\=\".*?\"".format(arg_chars)
    reg_no_quote = r"{0}+".format(arg_chars)
    # Matching args
    arguments_matching = re.findall(
        '({0}|{1}|{2}|".*?"|\'.*?\'|;|\n|'.format(
            reg_with_double_quote,
            reg_with_single_quote,
            reg_no_quote
        ) + '&{1,2}|\|)' + '($|)',
        cmd
    )
    normalized_cmd = [
        match[0] for match in arguments_matching
    ]
    # Normalizing no quote args
    normalized_cmd = [
        re.sub(reg_noquote_for_replace, '\\1"\\2"', arg)
        for arg in normalized_cmd
    ]
    # Normalizing single quote args
    normalized_cmd = [
        re.sub(reg_single_for_replace, '\\1"\\2"', arg)
        for arg in normalized_cmd
    ]
    # Normalize return;
    normalized_cmd = [
        re.sub('\n', ';', arg)
        for arg in normalized_cmd
    ]

    if normalized_cmd[-1] == ';':
        normalized_cmd.pop()

    return normalized_cmd


def normalize_shell_cmd_args_unique(cmd):
    cmds_separators = [';', '&', '&&', '|']
    args_list = normalize_shell_cmd_args(cmd)
    unique_args_list = [args_list[0]]
    for i in range(1, len(args_list)):
        arg = args_list[i]
        if (
            # Separators should be kept
            (arg in cmds_separators) or
            # Every command start should be kept (one with a sep before it)
            (args_list[i-1] in cmds_separators) or
            # We add not yet added
            (arg not in unique_args_list)
        ):
            unique_args_list.append(arg)
    return unique_args_list


def buildStrCmdFromList(args_list):
    cmd_out = ''
    for i in range(0, len(args_list) - 1):
        arg = args_list[i]
        if args_list[i+1] not in [';']:
            cmd_out += (arg + ' ')
        else:
            cmd_out += arg
    last_arg = args_list[len(args_list) - 1]
    cmd_out += last_arg
    return cmd_out


def normalize_shell_cmd(cmd):
    return buildStrCmdFromList(
        normalize_shell_cmd_args(cmd)
    )


def normalize_shell_cmd_unique(cmd):
    return buildStrCmdFromList(
        normalize_shell_cmd_args_unique(cmd)
    )


class FilterModule(object):
    def filters(self):
        return {
            'normalize_shell_cmd': normalize_shell_cmd,
            'normalize_shell_cmd_args': normalize_shell_cmd_args,
            'normalize_shell_cmd_unique': normalize_shell_cmd_unique,
            'normalize_shell_cmd_args_unique': normalize_shell_cmd_args_unique
        }

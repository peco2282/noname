from discord.ext import commands


def permissions(ctx: commands.Context) -> list:
    """The user's permissions value.
    Parameters
    ----------
    ctx : commands.Context
        The user's permissions

    Returns
    -------
    type : list
    string: :class:`str`
        return `str` the user's permissions.
    val: :class:`int`
        return `int` the user's permission value.
    """
    string = ''
    val = 0
    permission = ctx.author.guild_permissions
    string += '**General Channel Permissions**\n'

    if permission.manage_permissions:
        string += '`ロール (権限)の管理`, '
        val += 268435456

    if permission.view_channel or permission.read_messages:
        string += '`チャンネルを見る`, '
        val += 1024

    if permission.manage_channels:
        string += '`チャンネルを管理`, '
        val += 16

    if permission.manage_emojis_and_stickers:
        string += '`絵文字・スタンプの管理`, '
        val += 1073741824

    if permission.view_audit_log:
        string += '`監査ログを表示`, '
        val = 128

    if permission.manage_webhooks:
        string += '`ウェブフックの管理`, '
        val = 536870912

    if permission.manage_guild:
        string += '`サーバー管理`, '
        val += 32

    if permission.view_guild_insights:
        string += '`サーバーインサイトを見る`, '
        val += 524228

    string += '\n\n**Membership Permissions**\n'

    if permission.create_instant_invite:
        string += '`招待の作成`, '
        val += 1

    if permission.change_nickname:
        string += '`ニックネームの変更`, '
        val += 67108864

    if permission.manage_nicknames:
        string += '`ニックネームの管理`, '
        val += 134217728

    if permission.kick_members:
        string += '`メンバーをキック`, '
        val += 2

    if permission.ban_members:
        string += '`メンバーをBAN`, '
        val += 4

    string += '\n\n**Text Channel Permissions**\n'

    if permission.send_messages:
        string += '`メッセージの送信`, '
        val += 2048

    if permission.send_messages_in_threads:
        string += '`スレッドにメッセージを送信`, '
        val += 274877906944

    if permission.create_public_threads:
        string += '`公開スレッドの作成`, '
        val += 34359738368

    if permission.create_private_threads:
        string += '`プライベートスレッドの作成`, '
        val += 68719476736

    if permission.embed_links:
        string += '`埋め込みリンク`, '
        val += 16384

    if permission.attach_files:
        string += '`ファイルを添付`, '
        val += 32768

    if permission.add_reactions:
        string += '`リアクションの追加`, '
        val += 64

    if permission.use_external_emojis:
        string += '`外部の絵文字を使用`, '
        val += 262144

    a = [string, val]
    return a

